
import numpy as np

class system:
    def __init__(self, qargs):
        self.qargs = qargs
        self.stateket = qargs[0].value
        for i in range(1, len(qargs)):
            self.stateket = np.kron(self.stateket, qargs[i].value)
        self.density = self.stateket.dot(self.stateket.conj().T)
    def __repr__(self):
        return self.density.__str__()