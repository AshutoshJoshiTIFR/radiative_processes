import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

q = 4.803e-10
c = 29979245800
m = 9.108e-28

def alpha_nu(nu, p, B, C):
    t1 = (np.sqrt(3) * q**3) / (8 * np.pi * m)
    t2 = ((3 * q) / (2 * np.pi * m**3 * c**5)) ** (p/2) * C
    t3 = gamma((3 * p + 2)/12) * gamma((3 * p + 22)/12) * nu ** (-(p+4)/2)
    
    return t1 * t2 * t3 * B**((p+2)/2)
    

def Cs(L, B):
    C1 = 50 * L**3 / (3.91e28 + 1.64*1e41 * B**(-0.75))
    C2 = C1 * 1.426e-7 * B**(-0.75)    
    return [C1, C2]
    
def tau_nu(nu, p, B, C, L):
    return alpha_nu(nu, p, B, C) * L
    

nu_vals_1 = np.linspace(1e7, 1e10)
nu_vals_2 = np.linspace(1e10, 1e12)

p1 = 2.5
p2 = 4

L = 1e15
B = 1e-5
C1, C2 = Cs(L, B)

tau_nu_vals_1 = tau_nu(nu_vals_1, p1, B, C1, L)
tau_nu_vals_2 = tau_nu(nu_vals_2, p2, B, C2, L)

plt.plot(nu_vals_1, tau_nu_vals_1, ".-k")
plt.plot(nu_vals_2, tau_nu_vals_2, ".-k")

plt.xlabel("Frequency(Hz)")
plt.ylabel("Optical Depth")
plt.grid()
plt.title(f"B={B}G, L={L}cm")
plt.xscale("log")
plt.yscale("log")
plt.savefig("prob7_case4.png")
