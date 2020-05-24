

# Generate a truly random bit with given probabilities

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from math import pi

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



byte = generate_random(0.5, 7) + generate_random(0.3) # Generate a byte with a 30% change of being even
n = int(byte, 2)
print(n)


