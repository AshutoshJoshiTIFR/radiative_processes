import numpy as np
import matplotlib.pyplot as plt

C = 1.7 * 10**-23 / 5  # scaling constant

# Frequencies from 1e2 MHz to 1e9 MHz
nu = np.arange(10.**2, 10.**9, 500)

# Temperatures(K)
T1 = 1.e3
T2 = 1.e5

# Lengths(km)
L_A = 100
L_B = 1e10

# Optical depth expressions for free-free emission
def tau(L, T, nu):
    return C * (L / 1000)**4 * (T**-1.5) * (nu**-2) * L * 10.**5


tau_A_T1 = tau(L_A, T1, nu)
tau_A_T2 = tau(L_A, T2, nu)
tau_B_T1 = tau(L_B, T1, nu)
tau_B_T2 = tau(L_B, T2, nu)


plt.plot(nu, tau_A_T1, label='A: L=1e2 km, T=1e3 K')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (MHz)')
plt.ylabel(r'$ \tau_\nu$')
plt.title('Optical Depth vs Frequency')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()


plt.plot(nu, tau_A_T2, label='A: L=1e2 km, T=1e5 K')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (MHz)')
plt.ylabel(r'$ \tau_\nu$')
plt.title('Optical Depth vs Frequency')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()


plt.plot(nu, tau_B_T1, label='B: L=1e10 km, T=1e3 K')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (MHz)')
plt.ylabel(r'$ \tau_\nu$')
plt.title('Optical Depth vs Frequency')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()


plt.plot(nu, tau_B_T2, label='B: L=1e10 km, T=1e5 K')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Frequency (MHz)')
plt.ylabel(r'$ \tau_\nu$')
plt.title('Optical Depth vs Frequency')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()

