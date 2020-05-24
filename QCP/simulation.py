
import threading
from QRNG.QRNG import QRNG
from protocols.BB84 import BB84
from time import sleep

class agent(threading.Thread):
    def __init__(self, name, protocol):
        threading.Thread.__init__(self)
        self.name = name
        self.protocol = protocol


class Alice(agent):
    def __init__(self, name, protocol):
        super().__init__(name, protocol)

    def run(self):
        print("Generating key")
        key = QRNG.random(16)
        print("Key: " + key)
        key = self.protocol.send(key)
        print("Alice key: " + key.__str__())


class Bob(agent):
    def __init__(self, name, protocol):
        super().__init__(name, protocol)

    def run(self):
        key = self.protocol.recive()
        print("Bob key: " + key.__str__())

class Eve(agent):
    def __init__(self, name, protocol):
        super().__init__(name, protocol)

    def run(self):
        channel = self.protocol.qc
        key = channel.recive()
        print("Eve key: " + key.__str__())



protocol = BB84(16, 0.3)
alice = Alice("alice", protocol)
bob = Bob("bob", protocol)
eve = Eve("eve", protocol)
alice.start()
sleep(5)
eve.start()
sleep(5)
bob.start()
alice.join()
bob.join()
eve.join()