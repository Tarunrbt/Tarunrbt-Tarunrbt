import numpy as np

class ResponsePotential:
    """
    MOSGM-II Response Potential

    Psi_Omega = alpha * Phi_N * S(Omega)

    where:
    alpha  -> response strength
    Omega  -> environment metric
    S()    -> saturation function
    """

    def __init__(self, alpha=0.1):
        self.alpha = alpha

    # -------------------------------
    # Saturation function S(Omega)
    # -------------------------------
    def saturation(self, omega):
        """
        Sigmoid bounded response
        Using tanh ensures:
        - bounded behaviour
        - smooth transition
        """
        return np.tanh(omega)

    # -------------------------------
    # Response potential Psi_Omega
    # -------------------------------
    def psi_response(self, phi_newton, omega):
        return self.alpha * phi_newton * self.saturation(omega)

    # -------------------------------
    # Effective modified potential
    # -------------------------------
    def effective_potential(self, phi_newton, omega):
        return phi_newton + self.psi_response(phi_newton, omega)

    # -------------------------------
    # Modified acceleration
    # -------------------------------
    def modified_acceleration(self, grad_phi_newton, phi_newton, omega):
        """
        grad_phi_newton -> gradient of Newtonian potential
        """
        S = self.saturation(omega)
        return grad_phi_newton * (1 + self.alpha * S)
