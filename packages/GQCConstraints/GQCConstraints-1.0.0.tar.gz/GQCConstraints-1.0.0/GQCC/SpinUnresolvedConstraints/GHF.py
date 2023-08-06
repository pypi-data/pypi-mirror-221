"""
Spin unresolved constraints applied to generalized Hartree-Fock calculations.
------------------------------------------------------------------------

This class sets up everything needed for a Constrained GHF calculation. The required variables (Hamiltonian, Basis,...), as well as the required methods. 

"""

# Import statements
import gqcpy
import numpy as np
import numpy.random as rand

from GQCC.Optimization.SpinUnresolvedOptimizer import SpinUnresolvedOptimizer


class GHF(SpinUnresolvedOptimizer):
    """
    A constructor that sets up everything needed for constrained GHF calculations.

    :param molecule:                    The GQCP molecule used for the calculations.
    :param SQ_basis:                    The second quantized GQCP basis set used for the calculations, defined for a molecule in a certain basis set. Make sure it is the same basis as in which the operator is defined.
    :param solver:                      The solver used for the UHF calculations.
    :param initial_guess:               The initial guess for the UHF calculation.
    :param operator:                    The GQCP operator that will be constrained.     
    :param constrained_observable:      The name of the observable being constrained.
    :param stability_analysis:          Boolean flag denoting whether stability analysis is performed. Default is `True`.


    :returns:                An object which contains all required data (basis, Hamiltonian,... ) and possesses the necessary methods to perform calculations.
    """
    def __init__ (self, molecule, SQ_basis, solver, initial_guess, operator, constrained_observable, stability_analysis=True):
        # Check compatibility of the operator type based on the used basis type.
        if type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_d:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_d, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_d]
            assert (type(solver) is gqcpy.gqcpy.IterativeAlgorithm_GHFSCFEnvironment_d)

        elif type(SQ_basis) is gqcpy.gqcpy.GSpinorBasis_cd:
            compatible_operators = [gqcpy.gqcpy.ScalarGSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarGSQTwoElectronOperator_cd]
            assert (type(solver) is gqcpy.gqcpy.IterativeAlgorithm_GHFSCFEnvironment_cd)

        else:
            raise ValueError("the chosen `SQ_basis` or `solver` is not compatible with this type of calculation. Use `gqcpy.GSpinorBasis_(c)d`instead.")
        assert (type(operator) in compatible_operators), "Only `ScalarGSQOneElectronOperator_(c)d` or `ScalarGSQTwoElectronOperator_(c)d` can be constrained with this method."     

        # This basis can now quantize the Hamiltonian.
        self._sq_hamiltonian = SQ_basis.quantize(gqcpy.FQMolecularHamiltonian(molecule))

        # We will need the number of electrons, as well as the total number of Spinors later on.        
        self._K = SQ_basis.numberOfSpinors()
        self._N = molecule.numberOfElectrons()

        # Save the overlap and nuclear repulsion operators. 
        self._nuclear_repulsion = gqcpy.NuclearRepulsionOperator(molecule.nuclearFramework()).value()
        self._overlap = SQ_basis.quantize(gqcpy.OverlapOperator())

        # Save the operator you want to constrain.
        self._operator = operator
        self._constrained_observable = constrained_observable

        # Select the type of solver for the SCF algorithm.
        self._solver = solver
        self._initial_guess = initial_guess

        # Wheter to perform a stability check for each calculation.
        self._stability_analysis = stability_analysis


    # A solver for the GHF problem.
    # The GHF solver always takes a random guess, in order to activate the `off-diagonal` blocks. 
    def _solveGHFProblem(self, hamiltonian):
        """
        A method used to solve the iterative GHF problem. A stability check is performed automatically. If an internal instability is encountered, it will be followed by rotating the coefficeints in the direction of the lowest Hessian eigenvector. This will be shown in the output.

        :param hamiltonian:      The GSQHamiltonian used for the calculation.

        :returns:                The ground state energy.
        :returns:                The ground state parameters
        """

        # To solve the GHF problem we need an environment and a solver.
        if type(hamiltonian) is gqcpy.gqcpy.GSQHamiltonian_d:
            environment = gqcpy.GHFSCFEnvironment_d(self._N, hamiltonian, self._overlap, self._initial_guess)
            qc_structure = gqcpy.GHF_d.optimize(self._solver, environment)
        else:
            environment = gqcpy.GHFSCFEnvironment_cd(self._N, hamiltonian, self._overlap, self._initial_guess)
            qc_structure = gqcpy.GHF_cd.optimize(self._solver, environment)

        if self._stability_analysis:
            # For generalized Hartree-Fock, a stability check is always performed.
            # Transform the hamiltonian to MO basis and calculate the stability matrices. Print the resulting stabilities of the wavefunction model.
            coefficients = qc_structure.groundStateParameters().expansion()
            MO_hamiltonian = hamiltonian.transformed(coefficients)
            stability_matrices = qc_structure.groundStateParameters().calculateStabilityMatrices(MO_hamiltonian)

            internal_stability = stability_matrices.isInternallyStable(-1e-5)

            while internal_stability is False:
                print("**************************************************************")
                print("There is an internal instability. Follow it using the Hessian.")
                print("**************************************************************")

                # Rotate the coefficients in the direction of the lowest Hessian eigenvector.
                rotation = stability_matrices.instabilityRotationMatrix(self._N, self._K-self._N)
                coefficients_rotated = coefficients.rotated(rotation)

                # Perform a new SCF calculation with the rotated coefficients as initial guess.
                if type(hamiltonian) is gqcpy.gqcpy.GSQHamiltonian_d:
                    environment_rotated = gqcpy.GHFSCFEnvironment_d(self._N, hamiltonian, self._overlap, coefficients_rotated)
                    qc_structure = gqcpy.GHF_d.optimize(self._solver, environment_rotated)
                else:
                    environment_rotated = gqcpy.GHFSCFEnvironment_cd(self._N, hamiltonian, self._overlap, coefficients_rotated)
                    qc_structure = gqcpy.GHF_cd.optimize(self._solver, environment_rotated)

                coefficients_2 = qc_structure.groundStateParameters().expansion()

                # Perform a new stability check. Print the resulting stabilities.
                hamiltonian_MO_2 = hamiltonian.transformed(coefficients_2)
                stability_matrices_2 = qc_structure.groundStateParameters().calculateStabilityMatrices(hamiltonian_MO_2)

                # Print the new stability consitions.
                stability_matrices_2.printStabilityDescription()

                # Update the internal stability parameter.
                internal_stability = stability_matrices_2.isInternallyStable(-1e-5)

                if internal_stability:
                    print("**************************************************************")

        return qc_structure.groundStateEnergy(), qc_structure.groundStateParameters()


    # A function to calculate the energy and expectation value value of GHF at a certain multiplier. 
    def calculateEnergyAndExpectationValue(self, multiplier, return_parameters=False, verbose=0):
        """
        A method used to calculate the energy and the expectation value at a given multiplier `mu`.

        :param multiplier:      The multiplier used to modify the Hamiltonian.
        :param verbose:         An integer representing the amount of output that will be printed.
        :return_parameters:     A boolean flag that specifies whether the wavefunction parameters are also returned.

        :returns:               The energy at the given `mu` values.
        :returns:               The expectation value of the operator at the given `mu` value.
        :returns:               The wavefunction parameters (only if `return_parameters` is set to `True`).
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

        
        gs_energy, gs_parameters = self._solveGHFProblem(modified_hamiltonian)

        # Calculate the expectation value of the operator.
        DM = gs_parameters.calculateScalarBasis1DM()
        expectation_value = self._operator.calculateExpectationValue(DM)[0]

        # Perform the energy correction
        energy = gs_energy + ((multiplier * expectation_value) + self._nuclear_repulsion)

        # Print the progress of which mu values have been completed if verbose >= 2.
        if verbose >= 2:
            print("--------------------------------------------------------")
            print("Mu = " + str(np.around(multiplier, 2)) + " done.")

        if return_parameters:
            return energy, expectation_value, gs_parameters
        else:
            return energy, expectation_value
