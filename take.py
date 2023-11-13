class Taker():
    def __init__(self, que):
        self.queue = que
    
    def run(self):
        while True:
            print(self.queue.get())