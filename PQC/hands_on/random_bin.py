

# Generate a truly random bit with given probabilities

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from math import pi
from qubit import qubit

def generate_random(p_0, n=1):
    'Generates an n bit string for which each bit has a p_0 probability of being 0 '
    # Probability of 1
    p_1 = 1 - p_0

    # Generate circuit
    q = QuantumRegister(n)
    c = ClassicalRegister(n)
    qc = QuantumCircuit(q, c, name="Random Generator")

    # Calculate the angle
    angle = p_1 * pi

    # Rotate 'angle' radiants around the y axis to get the desired amplitude
    qc.ry(angle, q)

    # Read the qbit
    qc.measure(q, c)

    # Get backend
    backend = Aer.get_backend("qasm_simulator")

    #
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts()
    return list(counts.keys())[0]


def random_bell(n=1, p_0=0.5):
    'Generates a bell state with random amplitudes and returns a tuple with each pair of n qubits entangled'

    # Probability of 1
    p_1 = 1 - p_0

    c = QuantumRegister(n)
    t = QuantumRegister(n)

    qc = QuantumCircuit(c, t, name="Random bell pair generator")

    angle = p_1 * pi

    qc.ry(angle, c)
    for i in range(n):
        qc.cx(c[i], t[i])

    qc.measure_all()

    # Get backend
    backend = Aer.get_backend("qasm_simulator")

    #
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts()
    s  = list(counts.keys())[0]
    mid = int(len(s)/2)
    return (s[:mid], s[mid:])


def execute_qubit(q):
    
    qc = QuantumCircuit(q)
    print(qc)
    # Read the qbit
    qc.measure_all()

    # Get backend
    backend = Aer.get_backend("qasm_simulator")

    #
    job = execute(qc, backend, shots=1)
    counts = job.result().get_counts()
    return list(counts.keys())[0]

# Ex1
byte = generate_random(0.5, 7) + generate_random(0.3) # Generate a byte with a 30% change of being even
n = int(byte, 2)
print(n)

# Ex2

(a, b) = random_bell(8)

print(int(a, 2).__str__() + " == " + int(b, 2).__str__())

