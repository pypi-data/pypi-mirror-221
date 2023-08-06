"""
Spin Resolved Constraints applied to unrestricted Hartree-Fock
--------------------------------------------------------------

This class sets up everything needed for a spin resolved Constrained UHF calculation. The required variables (Hamiltonian, Basis,...), as well as the required methods. 

"""

# Import statements
import gqcpy
import numpy as np
import numpy.random as rand

from GQCC.Optimization.SpinResolvedOptimizer import SpinResolvedOptimizer


class UHF(SpinResolvedOptimizer):
    """
    A constructor that sets up everything needed for constrained UHF calculations.

    :param molecule:                    The GQCP molecule used for the calculations.
    :param electrons:                   The amount of alpha and beta electrons in the molecule as an array.
    :param SQ_basis:                    The second quantized GQCP basis set used for the calculations, defined for a molecule in a certain basis set. Make sure it is the same basis as in which the operator is defined.
    :param solver:                      The solver used for the UHF calculations.
    :param initial_guess:               The initial guess for the UHF calculation.
    :param operator:                    The GQCP operator that will be constrained.     
    :param constrained_observable:      The name of the observable being constrained.
    :param stability_analysis:          Boolean flag denoting whether stability analysis is performed. Default is `True`.

    :returns:                           An object which contains all required data (basis, Hamiltonian,... ) and possesses the necessary methods to perform calculations.
    """
    def __init__(self, molecule, electrons, SQ_basis, solver, initial_guess, operator, constrained_observable, stability_analysis=True):
        # Raise an exception if the electrons array is not conform with the requirements.
        if type(electrons[0]) is float or type(electrons[1]) is float or len(electrons) != 2:
            raise ValueError("Electrons must be of dimension 2 and must contain two ìnt`s as it must contain the number of alpha and beta electrons.")
        
        # Check compatibility of the operator type based on the used basis type.
        if type(SQ_basis) is gqcpy.gqcpy.USpinOrbitalBasis_d:
            compatible_operators = [gqcpy.gqcpy.ScalarUSQOneElectronOperator_d, gqcpy.gqcpy.ScalarUSQTwoElectronOperator_d]
            assert (type(solver) is gqcpy.gqcpy.IterativeAlgorithm_UHFSCFEnvironment)

        elif type(SQ_basis) is gqcpy.gqcpy.USpinOrbitalBasis_cd:
            compatible_operators = [gqcpy.gqcpy.ScalarUSQOneElectronOperator_cd, gqcpy.gqcpy.ScalarUSQTwoElectronOperator_cd]
            assert (type(solver) is gqcpy.gqcpy.IterativeAlgorithm_UHFSCFEnvironment_cd)

        else:
            raise ValueError("the chosen `SQ_basis` or `solver` is not compatible with this type of calculation. Use `gqcpy.USpinOrbitalBasis_(c)d`instead.")
        assert (type(operator) in compatible_operators), "Only `ScalarUSQOneElectronOperator_(c)d` or `ScalarUSQTwoElectronOperator_(c)d` can be constrained with this method."     

        # This basis can now quantize the Hamiltonian.
        self._sq_hamiltonian = SQ_basis.quantize(gqcpy.FQMolecularHamiltonian(molecule))

        # We will need the number of electrons, as well as the total number of Spinors later on.        
        self._Ka = SQ_basis.numberOfSpinors() // 2
        self._Kb = SQ_basis.numberOfSpinors() // 2

        self._Na = electrons[0]
        self._Nb = electrons[1]

        # Save the overlap and nuclear repulsion operators. 
        self._nuclear_repulsion = gqcpy.NuclearRepulsionOperator(molecule.nuclearFramework()).value()
        self._overlap = SQ_basis.quantize(gqcpy.OverlapOperator())

        # Save the operator you want to constrain.
        self._operator = operator

        self._constrained_observable = constrained_observable
        self._constrained_alpha_observable = "alpha " + self._constrained_observable
        self._constrained_beta_observable = "beta " + self._constrained_observable

        # Select the type of solver for the SCF algorithm and where to start the iterations.
        self._solver = solver
        self._initial_guess = initial_guess

        # Wheter to perform a stability check for each calculation.
        self._stability_analysis = stability_analysis


    # A solver for the UHF problem.
    def _solveUHFProblem(self, hamiltonian):
        """
        A method used to solve the iterative UHF problem. A stability check is performed automatically. If an internal instability is encountered, it will be followed by rotating the coefficeints in the direction of the lowest Hessian eigenvector. This will be shown in the output.

        :param hamiltonian:      The USQHamiltonian used for the calculation.

        :returns:                The ground state energy.
        :returns:                The ground state parameters
        """

        # To solve the GHF problem we need an environment and a solver.
        if type(hamiltonian) is gqcpy.gqcpy.USQHamiltonian_d:
            environment = gqcpy.UHFSCFEnvironment_d(self._Na, self._Nb, hamiltonian, self._overlap, self._initial_guess)
            qc_structure = gqcpy.UHF_d.optimize(self._solver, environment)
        else:
            environment = gqcpy.UHFSCFEnvironment_cd(self._Na, self._Nb, hamiltonian, self._overlap, self._initial_guess)
            qc_structure = gqcpy.UHF_cd.optimize(self._solver, environment)

        if self._stability_analysis:
            # For unrestricted Hartree-Fock, a stability check can be performed.
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
                rotation = stability_matrices.instabilityRotationMatrix(self._Na, self._Nb, self._Ka-self._Na, self._Kb-self._Nb)
                coefficients_rotated = coefficients.rotated(rotation)

                # Perform a new SCF calculation with the rotated coefficients as initial guess.
                if type(hamiltonian) is gqcpy.gqcpy.USQHamiltonian_d:
                    environment_rotated = gqcpy.UHFSCFEnvironment_d(self._Na, self._Nb, hamiltonian, self._overlap, coefficients_rotated)
                    qc_structure = gqcpy.UHF_d.optimize(self._solver, environment_rotated)
                else:
                    environment_rotated = gqcpy.UHFSCFEnvironment_d(self._Na, self._Nb, hamiltonian, self._overlap, coefficients_rotated)
                    qc_structure = gqcpy.UHF_d.optimize(self._solver, environment_rotated)

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


    # A function to calculate the energy and expectation value value of UHF at a certain multiplier. 
    def calculateEnergyAndExpectationValue(self, multiplier_array, return_parameters=False, verbose=0):
        """
        A method used to calculate the energy and the expectation value at a given multiplier `mu`.

        :param multiplier_array:      The multiplier used to modify the Hamiltonian.
        :param verbose:               An integer representing the amount of output that will be printed.
        :return_parameters:           A boolean flag that specifies whether the wavefunction parameters are also returned.

        :returns:                     The energy at the given `mu` values.
        :returns:                     The alpha/beta expectation values at the given `mu` values.
        :returns:                     The total spin unresolved expectation value at the given `mu`.
        :returns:                     The wavefunction parameters (only if `return_parameters` is set to `True`).
        """
        # Raise an exception if the multiplier is not conform with the requirements.
        if type(multiplier_array) is float or len(multiplier_array) != 2:
             raise ValueError("Multiplier_array must be of dimension 2 as it must contain both an alpha and beta value.")

        # Modify the Hamiltonian with the given multiplier.
        # Do this respectively for the alpha and beta parts.
        if type(self._operator) in [gqcpy.gqcpy.ScalarUSQOneElectronOperator_d, gqcpy.gqcpy.ScalarUSQOneElectronOperator_cd]:
            unrestricted_operator = type(self._operator)((self._operator.alpha * multiplier_array[0]), (self._operator.beta * multiplier_array[1]))
            modified_hamiltonian = self._sq_hamiltonian - unrestricted_operator
        # Or a two electron operator.
        elif type(self._operator) in [gqcpy.gqcpy.ScalarUSQTwoElectronOperator_d, gqcpy.gqcpy.ScalarUSQTwoElectronOperator_cd]:
            raise NotImplementedError("This is to be implemented after the general refactor is done.")
        else:
            raise ValueError("Something went wrong with the operator type.")


        gs_energy, gs_parameters = self._solveUHFProblem(modified_hamiltonian)

        # Calculate the expectation value of the operator.
        D = gs_parameters.calculateScalarBasis1DM()

        total_expectation_value = self._operator.calculateExpectationValue(D)[0]
        alpha_expectation_value = self._operator.alpha.calculateExpectationValue(D.alpha)[0]
        beta_expectation_value = self._operator.beta.calculateExpectationValue(D.beta)[0]

        # Calculate the energy by correcting the ground state energy of the modified Hamiltonian.
        energy = gs_energy + (multiplier_array[0] * alpha_expectation_value) + (multiplier_array[1] * beta_expectation_value) + self._nuclear_repulsion

        # Print the progress of which mu values have been completed if verbose >= 2.
        if verbose >= 2:
            print("--------------------------------------------------------")
            print("Mu combo: alpha = " + str(np.around(multiplier_array[0], 2)) + " , beta = " + str(np.around(multiplier_array[1], 2)) + " done.")
        if return_parameters:
            return energy, [alpha_expectation_value, beta_expectation_value], total_expectation_value, gs_parameters
        else:
            return energy, [alpha_expectation_value, beta_expectation_value], total_expectation_value
