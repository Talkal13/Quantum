import threading
from protocols.QuantumTeleport import QuantumTeleport
from time import sleep
from qiskit import QuantumCircuit, QuantumRegister
from math import pi

class agent(threading.Thread):
    def __init__(self, name, protocol):
        threading.Thread.__init__(self)
        self.name = name
        self.protocol = protocol


class Alice(agent):
    def __init__(self, name, protocol):
        super().__init__(name, protocol)

    def run(self):
        res = self.protocol.send(self.set_state())
        print("Alice has teleported the data with result: " + res)

    def set_state(self):
        q = QuantumRegister(1)
        qc = QuantumCircuit(q)

        # Set up state
        qc.rx(2/3 * pi, q)
        return qc


class Bob(agent):
    def __init__(self, name, protocol):
        super().__init__(name, protocol)

    def run(self):
        self.protocol.recive()
        print("Bob has recive the qubit")
        print(self.protocol.measure_b())

def exec():
    protocol = QuantumTeleport()
    alice = Alice("alice", protocol)
    bob = Bob("bob", protocol)
    alice.start()
    sleep(5)
    bob.start()
    alice.join()
    bob.join()