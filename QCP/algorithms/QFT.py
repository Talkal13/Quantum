from ..helper.helper import bitfield
from qiskit import QuantumCircuit, QuantumRegister

def QFT(a, N):

    q = QuantumRegister(N)
    qc = QuantumCircuit(N)
    encode(a, N)
    



def encode(a, N):
    v = bitfield(a)
    q = QuantumRegister(N)
    qc = QuantumCircuit(q)

    for i in range(v):
        if (v[i]):
            qc.x(q[i])
    
    return qc


q = QuantumRegister(2)
qc = QuantumCircuit(q)
qc