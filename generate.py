import time

class Generater():
    def __init__(self, que):
        self.que = que

    def do(self):
        self.que.put(input("入力:"))