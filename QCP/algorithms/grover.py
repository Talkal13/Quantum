from qiskit import QuantumCircuit, QuantumRegister
from math import sqrt, pi, ceil

def Groover(n, O, iter=0):
    '''Executes groover algorithm using O as an oracle'''
    q = QuantumRegister(n)
    qc = QuantumCircuit(q, name="Grover iteration")
    qc.h(q)
    
    
    if (iter == 0): iter = sqrt(n)

    for _ in range(ceil(iter)):
        qc.append(O, q)
        qc.h(q)
        qc.x(q)
        qc.mcrz(pi, q[:-1], q[-1])
        qc.x(q)
        qc.h(q)
        qc.barrier()
    print(qc)
    return qc
    