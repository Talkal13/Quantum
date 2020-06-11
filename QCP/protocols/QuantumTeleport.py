from ERP.states.bell_state import bell_state
from qiskit import QuantumCircuit, QuantumRegister
from threading import Lock

class QuantumTeleport:
    def __init__(self):
        self.q = QuantumRegister(1)
        self.a = QuantumRegister(1)
        self.b = QuantumRegister(1)
        self.qc = QuantumCircuit(self.q, self.a, self.b, name="Quantum Teleport")
        erps = bell_state(2)
        self.qc.append(erps.qc, [self.a] + [self.b])
        self.lock = Lock()
        self.result = None

    def send(self, phi):
        self.lock.acquire()
        self.qc.append(phi, self.q)
        self.qc.cx(self.q, self.a)
        self.qc.h(self.q)
        self.result = self.measure()
        self.lock.release()

    def recive(self):
        if self.result is None: return
        if self.result == "00":
            pass
        elif self.result == "01":
            self.qc.x(self.b)
        elif self.result == "10":
            self.qc.z(self.b)
        else:
            self.qc.x(self.b)
            self.qc.z(self.b)xz

    def measure(self):
        cb = ClassicalRegister(2)
        self.qc.add_register(cb)
        self.qc.measure(self.q, cb[0])
        self.qc.measure(self.a, cb[0])
        (result, statevector) = self.execute()
        self.reset_qc(statevector)
        return result

    def reset_qc(self, statevector):
        st = StateVectorCircuit(statevector)
        self.qc = st.construct_circuit(register=self.q)
        


    def execute(self):
        backend = Aer.get_backend("statevector_simulator")
        job = execute(self.qc, backend, shots=1)
        result = job.result()
        counts = result.get_counts()
        statevector = result.get_statevector()
        return (list(counts)[0], statevector)