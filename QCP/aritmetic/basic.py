from qiskit import QuantumRegister, QuantumCircuit
from helper.helper import bitfield

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
        
    print(qc)
    return qc


def rest(a, b):
    ''' Rests a - b on 'a' register, if it can't handle it will overflow'''
    return sum(a, b).inverse()

def ifb(a, b, qc):
