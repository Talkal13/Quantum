
from ERP.states.bell_state import bell_state
from simulations import QKDP, QT_simulation
from aritmetic.basic import sum, add, sub, rest, mult
from aritmetic.boolean import xor, qor
from algorithms.grover import Grover

from qiskit import (Aer, ClassicalRegister, QuantumCircuit, QuantumRegister,
                    execute)

from qiskit.circuit.library.standard_gates import XGate

from qiskit.aqua.components.oracles import CustomCircuitOracle

#QT_simulation.exec()

# Get backend
backend = Aer.get_backend("qasm_simulator")

a = QuantumRegister(2)
b = QuantumRegister(2)
cq = QuantumRegister(4)
c = ClassicalRegister(8)
anc = QuantumRegister(1)
qc = QuantumCircuit(a, b, cq, anc, c)

qc.h(a)
qc.h(b)

qc.append(mult(2, 2), a[:] + b[:] + cq[:] + [anc])


# Oracle
oq = QuantumRegister(4)
ancq = QuantumRegister(1)
O = QuantumCircuit(oq, ancq)
O.x(oq[0])
O.x(oq[3])
O.append(XGate().control(4), oq[:] + [ancq])

#oracle = CustomCircuitOracle(variable_register=oq, output_register=ancq, circuit=O)
#g = Grover(4, O)

#qc.append(g, cq[:] + [anc])
qc.measure(a, c[:2])
qc.measure(b, c[2:4])
qc.measure(cq, c[4:])

print(qc)



# Execute
job = execute(qc, backend, shots=1024)
counts = job.result().get_counts()
print(counts)