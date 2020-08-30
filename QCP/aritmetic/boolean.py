from qiskit import QuantumCircuit, QuantumRegister

def qnot():

    q = QuantumRegister(1)
    qc = QuantumCircuit(q)
    qc.x(q)

    return qc

def xor():
    q = QuantumRegister(2)
    qc = QuantumCircuit(q)
    qc.cx(q[0], q[1])

    return qc

def qand():

    q = QuantumRegister(2)
    a = QuantumRegister(1)
    qc = QuantumCircuit(q, a)
    qc.ccx(q[0], q[1], a)

    return qc

def qor():
    q = QuantumRegister(2)
    a = QuantumRegister(1)
    qc = QuantumCircuit(q, a)
    qc.x(q)
    qc.ccx(q[0], q[1], a)
    qc.x(q)
    qc.x(a)

    return qc
