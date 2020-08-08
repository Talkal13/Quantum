
from ERP.states.bell_state import bell_state
from simulations import QKDP, QT_simulation
from aritmetic.basic import sum, add, sub, rest

from qiskit import (Aer, ClassicalRegister, QuantumCircuit, QuantumRegister,
                    execute)

#QT_simulation.exec()

a = QuantumRegister(4)
b = QuantumRegister(4)
c = ClassicalRegister(4)
qc = QuantumCircuit(a, b, c)

qc.append(add(6, 4), a)
qc.append(sub(1, 4), a)

qc.barrier()

qc.append(add(2, 4), a)

qc.barrier()

qc.append(sum(4, 4), a[:] + b[:])

qc.barrier()

qc.measure(a, c)

print(qc.decompose())

# Get backend
backend = Aer.get_backend("qasm_simulator")

#
job = execute(qc, backend, shots=1)
counts = job.result().get_counts()
print(counts)