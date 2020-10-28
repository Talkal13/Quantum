import numpy as np
import re
from math import log2

q = [np.array([[1, 0]]), np.array([[0, 1]])]

def parse_string(value):
    if (value[0] == '~'):
        value = value[1:]
        return (int(value), None)
    if (re.search(r'[2-9]', value) is None):
        return (int(value, base=2), len(value))
    return (int(value), None)
    

def generate_qubit(value, tensor=None):
    if (value == 0): qubit = q[0]
    elif (value == 1): qubit = q[1]
    else: qubit = np.kron(generate_qubit(value >> 1, None), q[value & 0x1])
    _, size = qubit.shape
    while (tensor is not None and tensor > log2(size)):
        qubit = np.kron(q[0], qubit)
        _, size = qubit.shape
    return qubit


    