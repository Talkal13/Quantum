from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute
from qiskit.aqua import Gover
from ..QCP.aritmetic.basic import mult

l = 3
N = 15

a = QuantumRegister(l)
b = QuantumRegister(l)
c = QuantumRegister(2*l)
ancilla = QuantumRegister(1)

qc = QuantumCircuit(a,b,c,ancilla)

qc.h(a)
qc.h(b)
qc.append(mult(a, b), a + b + c + ancilla)


    