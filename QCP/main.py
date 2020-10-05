
from ERP.states.bell_state import bell_state
from simulations import QKDP, QT_simulation
from aritmetic.basic import sum, add, sub, rest, mult
from aritmetic.boolean import xor, qor
from algorithms.grover import Grover

from qiskit import (Aer, ClassicalRegister, QuantumCircuit, QuantumRegister,
                    execute)

from qiskit.circuit.library.standard_gates import XGate, ZGate

from qiskit.aqua.components.oracles import CustomCircuitOracle

#QT_simulation.exec()

# Get backend
backend = Aer.get_backend("qasm_simulator")
statevector = Aer.get_backend("statevector_simulator")

a = QuantumRegister(4)
#b = QuantumRegister(2)
#cq = QuantumRegister(4)
#anc = QuantumRegister(1)
c = ClassicalRegister(4)
qc = QuantumCircuit(a, c)

qc.h(a)


# qc.append(mult(2, 2), a[:] + b[:] + cq[:] + [anc])

# Oracle
oq = QuantumRegister(4)
O = QuantumCircuit(oq, name="Oracle")
O.x(oq[0])
O.x(oq[3])
O.append(ZGate().control(3), oq[:])
O.x(oq[0])
O.x(oq[3])

# Diffusor
d = QuantumRegister(4)
Dif = QuantumCircuit(d, name="Diffusor")
Dif.x(d)
Dif.h(d)
Dif.append(ZGate().control(3), d[:])
Dif.x(d)
Dif.h(d)

#oracle = CustomCircuitOracle(variable_register=oq, output_register=ancq, circuit=O)
g = Grover(4, O)

qc.append(O, a)
qc.append(Dif, a)

qc.append(O, a)
qc.append(Dif, a)

qc.append(O, a)
qc.append(Dif, a)

job = execute(qc, statevector, shots=1024)

# qc.append(g, cq[:])
# qc.measure(a, c[:2])
# qc.measure(b, c[2:4])
# qc.measure(cq, c[4:])

qc.measure(a, c)

print(qc)



# Execute

jobc = execute(qc, backend, shots=1024)
st = job.result().get_statevector()
counts = jobc.result().get_counts()

print(counts)
print(st)