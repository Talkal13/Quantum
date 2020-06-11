from qutip import *
import numpy as np
import scipy
import matplotlib.colors
import scipy

#the gate
hadamard = qutip.qip.hadamard_transform()
# the hamilton operator describing the evolution during the hadamard gate
hamilton = Qobj(scipy.linalg.logm(hadamard.data.todense()), dims=hadamard.dims) / np.pi * 1.j

#create initial state vector
psi0 = (basis(2, 0)).unit()

# describing the gate as time evolution
def gate(t):
    return (-2*np.pi*1.j*hamilton*t).expm()

# hadamard gate for t = 0.5
# In[1]: gate(0.5)
# Out[3]: 
# Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 0.70710678  0.70710678]
#  [ 0.70710678 -0.70710678]]

# evolve the gate
n = 25
psi = [gate(t)*psi0 for t in np.linspace(0, 1., 2*n)]

# plotting the states. State evolution during the first hamadard gate is red. During second hadamard gate is blue
b = Bloch()
b.vector_color = [matplotlib.colors.to_rgba('r', alpha=i) for i in np.arange(n)/float(n)] + [matplotlib.colors.to_rgba('b', alpha=i) for i in np.arange(n)/float(n)]  + ['black']
b.add_states(psi)
b.add_states([(basis(2,0) + (basis(2,0) + basis(2,1)).unit()).unit()])

b.show()