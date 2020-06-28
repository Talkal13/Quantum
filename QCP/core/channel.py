
from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, Aer, execute

class channel:

    def __init__(self, n):
        self.channel = QuantumCircuit(n, name="Channel")
        self.n = n
        self.backend = Aer.get_backend("qasm_simulator")

    def send(self, key):
        for i in range(len(key)):
            if (key[i] == "1"):
                self.channel.x(i)

    def recive(self):
        self.channel.measure_all()
        job = execute(self.channel, self.backend, shots=1)
        counts = job.result().get_counts()
        return list(counts.keys())[0][::-1]

        


