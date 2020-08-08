from qiskit import QuantumCirquit, QuantumRegister


def QFT(n):
    q = QuantumRegister(n, name="q")
    c = QuantumCirquit(q, name="QFT")

    for i in range(0, n):
        c.h(q[i])
        for j in range(i + 1, n):
            


print()