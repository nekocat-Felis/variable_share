class Taker:
    def __init__(self, que):
        self.que = que
        
    def do(self):
        print(self.que.get())