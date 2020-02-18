from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

#Subroutines

# Carry
c_c = QuantumRegister(1)
a_c = QuantumRegister(1)
b_c = QuantumRegister(2)
carry = QuantumCircuit(c_c, a_c, b_c, name="carry")

carry.ccx(a_c[0], b_c[0], b_c[1])
carry.cx(a_c[0], b_c[0])
carry.ccx(c_c[0], b_c[0], b_c[1])
carry.cx(a_c[0], b_c[0])

# Carry -1
c_i = QuantumRegister(1)
a_i = QuantumRegister(1)
b_i = QuantumRegister(2)
carry_i = QuantumCircuit(c_i, a_i, b_i, name="carry_inverse")


carry_i.cx(a_i[0], b_i[0])
carry_i.ccx(c_i[0], b_i[0], b_i[1])
carry_i.cx(a_i[0], b_i[0])
carry_i.ccx(a_i[0], b_i[0], b_i[1])

# Sum
c_s = QuantumRegister(1)
a_s = QuantumRegister(1)
b_s = QuantumRegister(1)
sum_c = QuantumCircuit(c_s, a_s, b_s,  name="sum")

sum_c.cx(a_s[0], b_s[0])
sum_c.cx(c_s[0], b_s[0])

# Add

def Add(n):
    c_a = QuantumRegister(n)
    a_a = QuantumRegister(n)
    b_a = QuantumRegister(n+1)

    add = QuantumCircuit(c_a, a_a, b_a, name="add")

    #base case
    if (n == 1):
        add.append(carry, [c_a[0], a_a[0], b_a[0], b_a[1]])
        add.append(sum_c, [c_a[0], a_a[0], b_a[0]])
    else:
        add.append(carry, [c_a[0], a_a[0], b_a[0], b_a[1]])
        add.append(sum_c, [c_a[0], a_a[0], b_a[0]])
        add.append(Add(n-1), c_a[1:n] + a_a[1:n] + b_a[1:n+1])
        #add.append(carry, [c_a[0], a_a[0], b_a[0], b_a[1]])
        
    
    return add


c = QuantumRegister(2, name="c")
a = QuantumRegister(2, name="a")
b = QuantumRegister(3, name="b")

m = ClassicalRegister(3, name="m")

q = QuantumCircuit(c, a, b, m, name="add")

c_input = input("c> ")
a_input = input("a> ")
for i in range(0, 2):
    if (c_input[i] == "1"):
        q.x(c[1 - i])
    if (a_input[i] == "1"):
        q.x(a[1 - i])

q.append(Add(2), c[0:2] + a[0:2] + b[0:3])

q.measure(b, m)

print(q.decompose())

# Execute the circuit
job = execute(q, backend = Aer.get_backend('qasm_simulator'), shots=1)
result = job.result()

# Print the result
print(result.get_counts(q))