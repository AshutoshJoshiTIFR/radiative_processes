import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

q = 4.803e-10
c = 29979245800
m = 9.108e-28

def P(nu, p, C, B):
    omega = 2 * np.pi * nu
    t1 = (3 * q**3 * C * B) / (2 * np.pi * m * c**2 * (p+1))
    
    t2 = gamma(p/4 + 19/12) * gamma(p/4 - 1/12)
    
    t3 = ((m * c * omega) / (3 * q * B)) ** (-(p-1)/2)
    
    return t1 * t2 * t3
    

nu_vals_1 = np.linspace(1e7, 1e10)
nu_vals_2 = np.linspace(1e10, 1e12)

p1 = 2.5
p2 = 4

C1 = 1

def C2(B):
    return 352.88 * B **(-0.75)
    

B = 1e6

P_vals_1 = P(nu_vals_1, p1, C1, B)
P_vals_2 = P(nu_vals_2, p2, C2(B), B)

plt.plot(nu_vals_1, P_vals_1, ".-k")
plt.plot(nu_vals_2, P_vals_2, ".-k")
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Frequency nu (Hz)")
plt.ylabel("Total Power P(nu) (erg/s-cm^3-Hz)")
plt.title("Synchrotron Power Spectrum")
plt.grid()
plt.savefig("prob6_case2.png")
