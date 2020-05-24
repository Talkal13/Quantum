
from qiskit import QuantumRegister, QuantumCircuit, ClassicalRegister, Aer, execute
from random_bin import random_bin

class channel:

    def __init__(self, n):
        self.channel = QuantumCircuit(n, name="Channel")
        self.backend = Aer.get_backend("qasm_simulator")

    def get_channel(self):
        return self.channel

    def send(self, key):
        for i in range(key):
            if (key[i]):
                self.channel.x(i)

    def recive(self):
        c = ClassicalRegister(n)
        self.channel.
        


