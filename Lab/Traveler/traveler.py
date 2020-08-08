from qiskit import(
  QuantumCircuit,
  QuantumRegister,
  ClassicalRegister,
  execute,
  Aer)
from qiskit.visualization import plot_histogram

def Ud():
    v = QuantumRegister(2)
    f = QuantumRegister(1)
    c = QuantumCircuit(v, f, name="Ud")

    c.cnot(v[0], f)
    c.cnot(v[1], f)

    return c

def Uf_zero():
    v = QuantumRegister(1)
    ancilla = QuantumRegister(1)
    c = QuantumCircuit(v, ancilla, name="Uf_0")

    c.x(ancilla)
    c.h(ancilla)
    c.x(v)
    c.cx(v, ancilla)
    c.x(v)
    c.h(ancilla)

    return c

def Uf():
    v = QuantumRegister(1)
    ancilla = QuantumRegister(1)
    c = QuantumCircuit(v, ancilla, name="Uf")
    
    c.x(ancilla)
    c.h(ancilla)
    c.cx(v, ancilla)
    c.h(ancilla)
    c.x(ancilla)

    return c

def Us():
    d = QuantumRegister(1)
    a = QuantumRegister(1)
    c = QuantumCircuit(d, a, name="Us")
    
    c.h(d)
    c.append(Uf_zero(), [d, a])
    c.h(d)
    
    return c

v = QuantumRegister(2)
d = QuantumRegister(1)
a = QuantumRegister(1)
b = ClassicalRegister(2)
c = QuantumCircuit(v, d, a, b)

c.h(v)

c.append(Ud(), [v[0], v[1], d], [])
c.append(Uf(), [d, a])
c.append(Us(), [d, a])


#c.h()

#c.append(Us(), f)



# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')
# Map the quantum measurement to the classical bits

c.measure(d, b[0])

# Execute the circuit on the qasm simulator
job = execute(c, simulator, shots=1000)

# Grab results from the job
result = job.result()
backend_sim = Aer.get_backend('statevector_simulator')
job_sim = execute(c, backend_sim)
statevec = job_sim.result().get_statevector()
print(statevec)


# Returns counts
counts = result.get_counts(c)

print(counts)
print(c.decompose())



