"""
Spin unresolved constraints applied on full configuration interaction calculations
-----------------------------------------------------------------------------

This class sets up everything needed for an unresolved constrained CI calculation. The required variables (Hamiltonian, ONV-Basis,...), as well as the required methods. 

"""

# Import statements
import gqcpy
import numpy as np

from GQCC.Optimization.SpinUnresolvedOptimizer import SpinUnresolvedOptimizer


class FCI(SpinUnresolvedOptimizer):
    """
    A constructor that sets up everything needed for spin unresolved constrained CI calculations.

    :param molecule:         The molecule used for the calculations.
    :param basis_set:        The basis set used for the calculations.
    :param operator:         The operator that will be constrained.
    :param basis:            The type of basis in which the FCI calculation will be performed. Default is restricted.

    :returns:                An object which contains all required data (basis, Hamiltonian,... ) and possesses the necessary methods to perform calculations.
    """
    def __init__(self, molecule, SQ_basis, operator, constrained_observable):
       # Check compatibility of the operator type based on the used basis_type.
        if type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_d:
            compatible_operators = [gqcpy.gqcpy.ScalarRSQOneElectronOperator_d, gqcpy.gqcpy.ScalarRSQTwoElectronOperator_d]
        elif type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_cd:
            compatible_operators = [gqcpy.gqcpy.ScalarRSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarRSQTwoElectronOperator_cd]
        elif type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_d:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_d, gqcpy.gqcpy.ScalarRSQTwoElectronOperator_d]
        elif type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_cd:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_cd]
        else:
            raise ValueError("the chosen `SQ_basis` is not compatible with this type of calculation. Use `gqcpy.R/GSpinOrbitalBasis_(c)d`instead.")
        
        assert (type(operator) in compatible_operators), "Only `ScalarR/GSQOneElectronOperator_(c)d` or `ScalarR/GSQTwoElectronOperator_(c)d` can be constrained with this method."

        # We can now create a first quantized hamiltonian and use the spin orbital basis to "quantize" it to second quantization.
        # The SQHamiltonian is stored in the class object.
        fq_hamiltonian = gqcpy.FQMolecularHamiltonian(molecule)
        self._sq_hamiltonian = SQ_basis.quantize(fq_hamiltonian)

        # Since we are going to do full CI calculations, we need an ONV-basis.
        # From the total number of orbitals and total number of electrons we can set up an ONV basis.
        if type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_d or type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_cd:
            K = int(SQ_basis.numberOfSpatialOrbitals())
        else:
            K = int(SQ_basis.numberOfSpinors())
        
        N_total = molecule.numberOfElectrons()

        if N_total % 2 == 0:
            N_a = int(N_total / 2)
            N_b = int(N_total / 2)
        else:
            N_a = int(np.ceil(N_total / 2))
            N_b = int(np.floor(N_total / 2))

        # The ONV basis gets stored within the class object.
        if type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_d or type(SQ_basis) is gqcpy.gqcpy.RSpinOrbitalBasis_cd:
            self._onv_basis = gqcpy.SpinResolvedONVBasis(K, N_a, N_b)
        else:
            full_onv_basis = gqcpy.SpinUnresolvedONVBasis(K, N_total)
            self._onv_basis = gqcpy.SpinUnresolvedSelectedONVBasis(full_onv_basis)

        # Calculate the nuclear repulsion term and store it in the class object.
        self._nuclear_repulsion = gqcpy.NuclearRepulsionOperator(molecule.nuclearFramework()).value()

        # Stor the operator that is being constrained.
        self._operator = operator
        self._constrained_observable = constrained_observable
    

    def _solveCIEigenproblem(self, hamiltonian):
        """
        A method used to solve a CI eigenproblem.

        :param hamiltonian:      The SQHamiltonian used for the calculation.

        :returns:                The ground state energy.
        :returns:                The ground state parameters
        """
        # Use GQCP to set up a full CI calculation.
        if type(hamiltonian) is gqcpy.gqcpy.RSQHamiltonian_d or type(hamiltonian) is gqcpy.gqcpy.GSQHamiltonian_d:
            CIsolver = gqcpy.EigenproblemSolver.Dense_d()
            CIenvironment = gqcpy.CIEnvironment.Dense(hamiltonian, self._onv_basis)
            qc_structure = gqcpy.CI(self._onv_basis).optimize(CIsolver, CIenvironment)
        else:
            CIsolver = gqcpy.EigenproblemSolver.Dense_cd()
            CIenvironment = gqcpy.CIEnvironment.Dense_cd(hamiltonian, self._onv_basis)
            qc_structure = gqcpy.CI_cd(self._onv_basis).optimize(CIsolver, CIenvironment)

        return qc_structure.groundStateEnergy(), qc_structure.groundStateParameters()
        

    def calculateEnergyAndExpectationValue(self, multiplier, return_parameters=False, verbose=0):
        """
        A method used to calculate the energy and the expectation value of the operator at a given multiplier `mu`.

        :param multiplier:              The multiplier used to modify the Hamiltonian.
        :param return_parameters:       A boolean flag to indicate whether only the wavefunction parameters should also be returned.
        :param verbose:                 An integer representing the amount of output that will be printed.

        :returns:                       The energy at the given `mu` value.
        :returns:                       The expectation value of the operator at the given `mu` value.
        :returns:                       The wavefunction parameters (only if `return_parameters` is set to `True`).
        """
        # Modify the Hamiltonian with the given multiplier.
        if type(self._operator) in [gqcpy.gqcpy.ScalarRSQOneElectronOperator_d, gqcpy.gqcpy.ScalarRSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarGSQOneElectronOperator_d, gqcpy.gqcpy.ScalarGSQOneElectronOperator_cd]:
            modified_hamiltonian = self._sq_hamiltonian - multiplier * self._operator
        # Or a two electron operator.
        elif type(self._operator) in [gqcpy.gqcpy.ScalarRSQTwoElectronOperator_d, gqcpy.gqcpy.ScalarRSQTwoElectronOperator_cd, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_d, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_cd]:
            raise NotImplementedError("This is to be implemented after the general refactor is done.")
        else:
            raise ValueError("Something went wrong with the operator type.")
        
        # Use the private method to solve the full CI eigenproblem.
        gs_energy, gs_parameters = self._solveCIEigenproblem(modified_hamiltonian)

        # Use the ground state parameters to calculate the 1DM and use it to calculate the expectation value of the Mulliken operator.
        D = gs_parameters.calculate1DM()
        W = self._operator.calculateExpectationValue(D)[0]

        # Calculate the energy by correcting the ground state energy of the modified Hamiltonian.
        energy = gs_energy + (multiplier * W) + self._nuclear_repulsion

        # Print the progress of which mu values have been completed if verbose >= 2.
        if verbose >= 2:
            print("--------------------------------------------------------")
            print("Mu = " + str(np.around(multiplier, 2)) + " done.")

        if return_parameters:
            return energy, W, gs_parameters
        else:
            return energy, W
