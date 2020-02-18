from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

q = QuantumRegister(2, name="q")
erp = QuantumCircuit(q, name="erp")

erp.h(q[0])
erp.cx(q[0], q[1])

