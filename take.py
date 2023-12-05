class Taker:
    def __init__(self, que):
        self.que = que
        
    def do(self):
        while True:
            print(self.que.get())