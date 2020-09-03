from qiskit import QuantumRegister, QuantumCircuit
from helper.helper import bitfield
from .boolean import qor

def add(k, n):
    ''' Generates a quantum circuit that adds k to n qubits where represents q[0] the less significant qubit'''
    q = QuantumRegister(n)
    qc = QuantumCircuit(q, name='Add(%i)' % k)

    bits = bitfield(k)[::-1]
    for i in range(len(bits)):
        if bits[i]:
            for k in reversed(range(i, len(bits))):
                qc.mct(q[i:k], q[k], None, mode='advanced')
            #qc.x(q[i])

    return qc

def sub(k, n):
    ''' Generates a quantum cirucuit that substracts k to n qubits where q[0] represents the less significant qubit'''  
    return add(2**n - k, n)




def sum(a, b):

    ''' Sums a + b on a register, if it can't handle it will overflow'''
    aq = QuantumRegister(a)
    bq = QuantumRegister(b)

    qc = QuantumCircuit(aq, bq, name="Sum(%i, %i)" % (a, b))

    for i in range(b):
        for j in reversed(range(i, a)):
            qc.mct(aq[i:j] + [bq[i]], aq[j], None, mode='advanced')

    return qc


def rest(a, b):
    ''' Rests a - b on 'a' register, if it can't handle it will overflow'''
    return sum(a, b).inverse()


def mult(a, b):
    aq = QuantumRegister(a)
    bq = QuantumRegister(b)
    cq = QuantumRegister(a + b)
    anc = QuantumRegister(1)

    qc = QuantumCircuit(aq, bq, cq, anc, name="Mult(%i, %i)" % (a, b))

    for _ in range(pow(2, b)):
        qc.append(qor(b), bq[:] + [anc])
        qc.append(sum(a+b, a).to_gate().control(1), [anc] + cq[:] + aq[:])
        qc.append(sub(1, b).to_gate().control(1), [anc] + bq[:])
        qc.reset(anc)
    
    print(qc)

    return qc

    
