import numpy as np
import matplotlib.pyplot as plt

def alpha(s, a0=1):
    if s<0:
        print("Invalid s")
        return
    out = a0 * s**2
    #out = a0 * np.log(s)
    return out
    
    
def sigma(s, sig0=1):
    if s<0:
        print("Invalid s")
        return
    out = sig0 * s**2
    #out = sig0 * np.log(s)
    return out
    

def rk4_solver(y_initial, x_range, dydx):
    """
    Solves an initial value problem using RK-4 Method.
    """
    n = np.size(x_range)
    y = np.zeros((n, len(y_initial)))
    h = x_range[1] - x_range[0]
    y[0] = y_initial
    for i in range(np.size(x_range) - 1):
        k1 = h * dydx(x_range[i], y[i])
        k2 = h * dydx(x_range[i] + h/2, y[i] + k1/2)
        k3 = h * dydx(x_range[i] + h/2, y[i] + k2/2)
        k4 = h * dydx(x_range[i+1], y[i] + k3)
        y[i+1] = y[i] + 1/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


def dydx(x, y):
    """
    For Problem 5, 6.
    y = [I_nu, tau_nu]
    x = s
    """
    S_nu = 0
    dy1 = - (alpha(x) + sigma(x)) * (y[0] - S_nu)
    dy2 = alpha(x) + sigma(x)
    
    return np.array([dy1, dy2])
    

# Solving with initial conditions
L = 10
I_nu_i = 1
tau_nu_i = 0

y_initial = np.array([I_nu_i, tau_nu_i])
s_range = np.linspace(0.1 * L, L, 10000)

y = rk4_solver(y_initial, s_range, dydx)

I_nu = y[:, 0]
tau_nu = y[:, 1]

plt.plot(s_range/L, tau_nu, ".-k")
plt.xlabel("r/L")
plt.ylabel("tau_nu")
plt.grid()
plt.show()

plt.plot(s_range/L, I_nu, ".-k")
plt.xlabel("r/L")
plt.ylabel("I_nu")
#plt.ylim(0, 1)
plt.grid()
plt.show()
