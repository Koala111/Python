class Data:
    def __init__(self, n):
      self.n = n

    def __getitem__(self, index):
        if index < 0 or index >= self.n : raise IndexError
        return index + 100


