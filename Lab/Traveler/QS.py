from qiskit inport QuantumCircuit, QuantumRegister
from math import ceil


def QValue(n, R):
    size = ceil(log(n)) * n
    v = QuantumRegister(size)
    r = QuantumRegister(R)
    c = QuantumCircuit(v)

    # TODO: f(x) = value of traveling in the order with precision R bits
    #Example asuming the fields are bidirectional:
    

