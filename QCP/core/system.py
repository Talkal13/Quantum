
from qiskit import QuantumCircuit

class qsystem(QuantumCircuit):
    
    def add_owned(self, id, n):
        self.add_register(QuantumRegister(n))
        self.owners[id].append(q)

    def measureOwn(self, q, id):
        if (self.)
