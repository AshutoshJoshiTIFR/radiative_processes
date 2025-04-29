import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def integrand1(r, j0, alpha0):
    """
    This function calculates the integrand of particular solution for
    radiative transfer equation for problem 2(a).
    :param r: distance
    :param j0: constant for emissivity
    :param alpha0: constant for absorption coefficient
    :return: integrand
    """
    return (j0 / r**2) * np.exp(tau1(r, alpha0))


def I_nu1(r, I_nu0, j0, alpha0, r0=10**-5):
    """
    This function solves the radiative transfer equation to obtain
    brightness for problem 2(a).
    :param r: distance
    :param I_nu0: Initial intensity at r0
    :param j0: constant for emissivity
    :param alpha0: constant for absorption coefficient
    :param r0: initial distance
    :return: brightness
    """
    integral_result, _ = quad(integrand1, r0, r, args=(j0,alpha0))
    return I_nu0 * np.exp(-tau1(r, alpha0)) + np.exp(-tau1(r, alpha0)) * integral_result

def tau1(r, alpha0):
    """
    This function calculates optical depth as a function of r for problem 2(a).
    :param r: distance
    :param alpha0: constant for absorption coefficient
    :return: optical depth
    """
    return alpha0 * r ** 2 / 2.


# Constants
I_nu0 = 1.0      # Initial intensity
alpha0 = 1.0    # constant for absorption coefficient
j0 = 1.0         # constant for emissivity
r_values = np.linspace(0.1, 1, 500)
I_values = np.array([I_nu1(r, I_nu0, j0, alpha0) for r in r_values])
tau_values = np.array([tau1(r, alpha0) for r in r_values])
plt.figure(figsize=(8, 5))
plt.plot(r_values, I_values, label=r'$I_{\nu}(r)$', color='navy')
plt.xlabel(r'$r/L$')
plt.ylabel(r'$I_{\nu}(r)$')
plt.title('Plot of $I_{\\nu}(r)$ from $0.1L$ to $L$')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(r_values, tau_values, label=r'$\tau_{\nu}(r)$', color='black')
plt.xlabel(r'$r/L$')
plt.ylabel(r'$\tau_{\nu}(r)$')
plt.title('Plot of $\\tau_{\\nu}(r)$ from $0.1L$ to $L$')
plt.grid(True)
plt.legend()
plt.show()



def tau2(r, alpha0):
    """
        This function calculates optical depth as a function of r for problem 2(b).
        :param r: distance
        :param alpha0: constant for absorption coefficient
        :return: optical depth
    """
    return alpha0 * (1 - np.exp(-r) * (1 + r))

# --- Define the integral inside the expression ---
def integrand2(r, j0, alpha0):
    """
        This function calculates the integrand of particular solution for
        radiative transfer equation for problem 2(a).
        :param r: distance
        :param j0: constant for emissivity
        :param alpha0: constant for absorption coefficient
        :return: integrand
    """
    return j0 * np.log(r) * np.exp(tau2(r, alpha0))

# --- Define the full I_nu(r) function ---
def I_nu2(r, I_nu0, j0, alpha0, r0=10**-5):
    """
    This function solves the radiative transfer equation to obtain
    brightness for problem 2(b).
    :param r: distance
    :param I_nu0: Initial intensity at r0
    :param j0: constant for emissivity
    :param alpha0: constant for absorption coefficient
    :param r0: initial distance
    :return: brightness
    """
    integral_result, _ = quad(integrand2, r0, r, args=(j0, alpha0))
    return I_nu0 * np.exp(-tau1(r, alpha0)) + np.exp(-tau1(r, alpha0)) * integral_result


# --- Set up r values ---
r_values = np.linspace(0.1, 1, 500)
I_values = np.array([I_nu2(r, I_nu0, j0, alpha0) for r in r_values])
tau_values = np.array([tau2(r, alpha0) for r in r_values])

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(r_values, I_values, label=r'$I_{\nu}(r)$', color='navy')
plt.xlabel(r'$r/L$')
plt.ylabel(r'$I_{\nu}(r)$')
plt.title('Plot of $I_{\\nu}(r)$ from $0.1L$ to $L$')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(r_values, tau_values, label=r'$\tau_{\nu}(r)$', color='black')
plt.xlabel(r'$r/L$')
plt.ylabel(r'$\tau_{\nu}(r)$')
plt.title('Plot of $\\tau_{\\nu}(r)$ from $0.1L$ to $L$')
plt.grid(True)
plt.legend()
plt.show()