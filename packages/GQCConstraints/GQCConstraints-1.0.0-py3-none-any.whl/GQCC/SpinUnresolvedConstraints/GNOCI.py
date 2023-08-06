"""
Spin unresolved constraints applied to Non-Orthogonal CI in a Generalized basis
-------------------------------------------------------------------------------

This class sets up everything needed for a Constrained NOCI calculation, based on Generalized states. The required variables (Hamiltonian, Basis,...), as well as the required methods. 

"""

# Import statements
import gqcpy
import numpy as np

from GQCC.Optimization.SpinUnresolvedOptimizer import SpinUnresolvedOptimizer


class GNOCI(SpinUnresolvedOptimizer):
    """
    A constructor that sets up everything needed for constrained NOCI calculations in a generalized basis.

    :param molecule:                    The GQCP molecule used for the calculations.
    :param SQ_basis:                    The second quantized GQCP basis set used for the calculations, defined for a molecule in a certain basis set. Make sure it is the same basis as in which the operator is defined.
    :param basis_state_vector:          A vector of non-orthogonal states that will serve as a basis for NOCI.
    :param operator:                    The GQCP operator that will be constrained.    
    :param constrained_observable:      The name of the observable being constrained.

    :returns:                       An object which contains all required data (basis, Hamiltonian,... ) and possesses the necessary methods to perform calculations.
    """
    def __init__(self, molecule, SQ_basis, basis_state_vector, operator, constrained_observable):
        # Check compatibility of the operator type based on the used basis type.
        if type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_d:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_d, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_d]
        elif type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_cd:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_cd]
        else:
            raise ValueError("the chosen `SQ_basis` or `solver` is not compatible with this type of calculation. Use `gqcpy.GSpinorBasis_(c)d`instead.")
        assert (type(operator) in compatible_operators), "Only `ScalarGSQOneElectronOperator_(c)d` or `ScalarGSQTwoElectronOperator_(c)d` can be constrained with this method."     

        # Here, a molecule does need to be saved as it is needed to construct the NOCI Hamiltonian.
        self._molecule = molecule

        # Save the number of electrons.
        self._N = molecule.numberOfElectrons()

        # Quantize the Hamiltonian in the spinor basis.
        self._sq_hamiltonian = SQ_basis.quantize(gqcpy.FQMolecularHamiltonian(molecule))

        # Save the overlap operator.
        self._overlap = SQ_basis.quantize(gqcpy.OverlapOperator())

        # Generate a Non-orthogonal state basis.
        self._NOCIBasis = gqcpy.GNonOrthogonalStateBasis_d(basis_state_vector, self._overlap, self._N)

        # Save the operator you want to constrain.
        self._operator = operator
        self._constrained_observable = constrained_observable


    # A solver for the NOCI problem.
    def _solveNOCIEigenproblem(self, hamiltonian):
        """
        A method used to solve a NOCI eigenproblem.

        :param hamiltonian:      The SQHamiltonian used for the calculation.

        :returns:                The ground state energy.
        :returns:                The ground state parameters
        """
        if type(hamiltonian) is gqcpy.gqcpy.GSQHamiltonian_d:
            environment = gqcpy.NOCIEnvironment.Dense_d(hamiltonian, self._NOCIBasis, self._molecule)
            solver = gqcpy.GeneralizedEigenproblemSolver.Dense_d()
            qc_structure = gqcpy.NOCI_d(self._NOCIBasis).optimize(solver, environment)
        else:
            environment = gqcpy.NOCIEnvironment.Dense_cd(hamiltonian, self._NOCIBasis, self._molecule)
            solver = gqcpy.GeneralizedEigenproblemSolver.Dense_cd()
            qc_structure = gqcpy.NOCI_cd(self._NOCIBasis).optimize(solver, environment)

        return qc_structure.groundStateEnergy(), qc_structure.groundStateParameters()

     
    # A function to calculate the energy and expectation value of NOCI at a certain multiplier. 
    def calculateEnergyAndExpectationValue(self, multiplier, return_parameters=False, verbose=0):
        """
        A method used to calculate the energy and the expectation value at a given multiplier `mu`.

        :param multiplier_array:      The multiplier used to modify the Hamiltonian.
        :param verbose:               An integer representing the amount of output that will be printed.
        :return_parameters:           A boolean flag that specifies whether the wavefunction parameters are also returned.

        :returns:                     The energy at the given `mu` values.
        :returns:                     The expectation value of the operator at the given `mu` value.
        :returns:                     The wavefunction parameters (only if `return_parameters` is set to `True`).
        """
        # Modify the Hamiltonian with the given multiplier.
        # Do this respectively for the alpha and beta parts.
        if type(self._operator) in [gqcpy.gqcpy.ScalarGSQOneElectronOperator_d, gqcpy.gqcpy.ScalarGSQOneElectronOperator_cd]:
            modified_hamiltonian = self._sq_hamiltonian - (multiplier * self._operator)
        # Or a two electron operator.
        elif type(self._operator) in [gqcpy.gqcpy.ScalarGSQTwoElectronOperator_d, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_cd]:
            raise NotImplementedError("This is to be implemented after the general refactor is done.")
        else:
            raise ValueError("Something went wrong with the operator type.")

        gs_energy, gs_parameters = self._solveNOCIEigenproblem(modified_hamiltonian)

        # Calculate the expectation value.
        DM = gs_parameters.calculate1DM()
        expectation_value = self._operator.calculateExpectationValue(DM)[0]

        # Perform the energy correction.
        energy = gs_energy  + (multiplier * expectation_value)

        # Print the progress of which mu values have been completed if verbose >= 2.
        if verbose >= 2:
            print("--------------------------------------------------------")
            print("Mu = " + str(np.around(multiplier, 2)) + " done.")

        if return_parameters:
            return energy, expectation_value, gs_parameters
        else:
            return energy, expectation_value
