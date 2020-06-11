
from ERP.states.bell_state import bell_state
from ERP.states.remote_controlled import remote_controlled
from simulations import QKDP

b = remote_controlled(2, 0.85)
print("Alice: " + b.measure([0]))
print("Bob: " + b.measure([1]))