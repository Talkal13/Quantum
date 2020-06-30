
from ..ERPS import ERPS
from math import pi, acos

class remote_controlled(ERPS):
    
    def __init__(self, n=1, p=0.5):
        super().__init__(n)
        self.p = 0.5
        self.prepare()

    def prepare(self):
        ''' state: \\frac{1}{2\\sqrt(2)}((1 + e^{i\\lambda})(|00> + |11>) + (1 - e^{i\\lambda})(|01> + |10>)) '''
        lamb = acos((self.p - 0.5)*2)
        self.qc.h(self.q)
        self.qc.rz(lamb, self.q[1])
        self.qc.h(self.q[1])
        self.qc.cx(self.q[0], self.q[1])
        