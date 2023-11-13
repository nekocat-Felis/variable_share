import time

class Generater():
    def __init__(self, que):
        self.queue = que
    
    def run(self):
        i = 0
        while True:
            self.queue.put(i)
            i += 1