import numpy as np

q = [np.array([[1, 0]]), np.array([[0, 1]])]
def generate_qubit(value):
    if (value == 0): return q[0]
    elif (value == 1): return q[1]
    return np.kron(generate_qubit(value >> 1), q[value & 0x1])