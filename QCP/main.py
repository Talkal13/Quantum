
from ERP.states.bell_state import bell_state
from simulations import QKDP, QT_simulation
from aritmetic.basic import sum, add, sub, rest
from aritmetic.boolean import xor
from algorithms.grover import Groover

from qiskit import (Aer, ClassicalRegister, QuantumCircuit, QuantumRegister,
                    execute)

#QT_simulation.exec()

# Get backend
backend = Aer.get_backend("qasm_simulator")

a = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(a, c)

O = QuantumCircuit(2)
O.x(1)
O.cz(0, 1)
O.x(1)

print(O)

qc.append(Groover(2, O), a)

qc.measure(a, c)

print(qc.decompose())



# Execute
job = execute(qc, backend, shots=1024)
counts = job.result().get_counts()
print(counts)