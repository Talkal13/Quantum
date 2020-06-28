from core.channel import channel
from QRNG.QRNG import QRNG
from math import ceil

class BB84:
    def __init__(self, n, assure=0.1):
        self.n = n
        self.sa = False
        self.rb = False
        self.rra = False
        self.rrb = False
        self.a = []
        self.b = []
        self.keya = []
        self.keyb = []
        self.assure = assure
        self.qc = channel(self.n) # Quantum channel
        self.cp = BB84_qc(self.n, self.qc) # Channel Protocol

    def send(self, key):
        self.sa = False
        self.a = []
        self.cp.send(key, self.a)
        self.sa = True
        while(not (self.sa and self.rb)): pass
        self.rra = False
        key = self.check_basis(key)
        self.keya = self.get_key(key)
        key = key[len(self.keyb):]
        self.rra = True
        while(not (self.rra and self.rrb)): pass
        return (key, self.check_key())
    
    def recive(self):
        self.rb = False
        self.b = []
        while(not self.sa): pass
        key = self.cp.recive(self.b)
        self.rb = True
        self.rrb = False
        key = self.check_basis(key)
        self.keyb = self.get_key(key)
        key = key[len(self.keyb):]
        self.rrb = True
        while(not (self.rra and self.rrb)): pass
        return (key, self.check_key())

    def check_key(self):
        for i in range(len(self.keya)):
            if (self.keya[i] != self.keyb[i]):
                return False
        return True


    def check_basis(self, key):
        new_key = []
        for i in range(self.n):
            if (self.a[i] == self.b[i]):
                new_key.append(key[i])
        return new_key

    def get_key(self, key):
        new_key = []
        for i in range(ceil(len(key) * self.assure)):
            new_key.append(key[i])
        return new_key



class BB84_qc:
    def __init__(self, n, channel):
        self.n = n
        self.channel = channel
    
    def send(self, key, a):
        self.channel.send(key)
        for i in range(self.n):
            if (QRNG.random() == "1"):
                self.channel.channel.h(i)
                a.append(1)
            else:
                a.append(0)
        

    def recive(self, b):
        for i in range(self.n):
            if (QRNG.random() == "1"):
                self.channel.channel.h(i)
                b.append(1)
            else:
                b.append(0)
        return self.channel.recive()
            