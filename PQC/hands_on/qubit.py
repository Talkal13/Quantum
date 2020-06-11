
from qiskit import QuantumRegister, QuantumCircuit, Aer, execute, ClassicalRegister

class qubit:
    def __init__(self, q, qc):
        self.q = q
        self.qc = qc

    def measure(self):
        c = ClassicalRegister(len(self.q))
        self.qc.measure(self.q, c)

        # Get backend
        backend = Aer.get_backend("qasm_simulator")

        #
        job = execute(self.qc, backend, shots=1)
        counts = job.result().get_counts()
        return list(counts.keys())[0]