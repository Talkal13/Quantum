from ..ERPS import ERPS

class bell_state(ERPS):

    def __init__(self, n=2):
        super().__init__(n)
        self.prepare()

    def prepare(self):
        self.qc.h(self.q[0])
        for i in range(1,self.n):
            self.qc.cx(self.q[0], self.q[i])
        