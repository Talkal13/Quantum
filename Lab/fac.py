from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer
from math import gcd
import numpy as np
from fractions import Fraction

''' 
    Implementacion del Algoritmo de Shor
    fuente: https://qiskit.org/textbook/ch-algorithms/shor.html
'''


def U_x15(a, j):
    '''
        Transformacion U_x15 |j>|k> -> |j>|a^{j}k (mod 15)> 
    '''
    U = QuantumCircuit(4)        
    for _ in range(j):
        if a in [2,13]:
            U.swap(0,1)
            U.swap(1,2)
            U.swap(2,3)
        if a in [7,8]:
            U.swap(2,3)
            U.swap(1,2)
            U.swap(0,1)
        if a == 11:
            U.swap(1,3)
            U.swap(0,2)
        if a in [7,11,13]:
            for q in range(4):
                U.x(q)
    U = U.to_gate()
    U.name = "%i^%i mod 15" % (a, j)
    c_U = U.control()
    return c_U

def QFT_Inversa(n):
    """
        QFT Inversa de n qubits
        
    """
    qc = QuantumCircuit(n)
    # Don't forget the Swaps!
    for qubit in range(n//2):
        qc.swap(qubit, n-qubit-1)
    for j in range(n):
        for m in range(j):
            qc.cu1(-np.pi/float(2**(j-m)), m, j)
        qc.h(j)
    qc.name = "QFT†"
    return qc


def periodo(a):
    n_count = 3
    qc = QuantumCircuit(4+n_count, n_count)
    for q in range(n_count):
        qc.h(q)     # Initialise counting qubits in state |+>
    qc.x(3+n_count) # And ancilla register in state |1>
    for q in range(n_count): # Do controlled-U operations
        qc.append(U_x15(a, 2**q), 
                 [q] + [i+n_count for i in range(4)])
    qc.append(QFT_Inversa(n_count), range(n_count)) # Do inverse-QFT
    qc.measure(range(n_count), range(n_count))
    # Simulate Results
    backend = Aer.get_backend('qasm_simulator')
    # Setting memory=True below allows us to see a list of each sequential reading
    result = execute(qc, backend, shots=1, memory=True).result()
    readings = result.get_memory()
    phase = int(readings[0],2)/(2**n_count)
    return phase

    
def shor():
    # Generar valores
    a = 7
    N = 15

    if (gcd(a, N) != 1): 
        # a es un factor no trivial de N
        print("%i es un factor no trivial de %i" % (a, N))
        return 

    factor_found = False
    attempt = 0
    while not factor_found:
        attempt += 1
        print("\nAttempt %i:" % attempt)
        phase = periodo(a) # periodo = s/r
        frac = Fraction(phase).limit_denominator(15) # Aplicar fracciones continuas
        r = frac.denominator
        print("Resultado: r = %i" % r)
        if phase != 0:
            # Posibles factores =  gcd(x^{r/2} ±1 , 15)
            guesses = [gcd(a**(r//2)-1, 15), gcd(a**(r//2)+1, 15)]
            print("Factores posibles: %i and %i" % (guesses[0], guesses[1]))
            for guess in guesses:
                if guess != 1 and (15 % guess) == 0:
                    print("*** Encontrado factor no trivial de 15: %i ***" % guess)
                    factor_found = True


shor()

    