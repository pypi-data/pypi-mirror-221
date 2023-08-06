class Operation:
    def __init__(self,val1,val2):
        self.value1 = val1
        self.value2 = val2
    def evaluate(self):
        raise NotImplementedError("Operation is a Abstract class")

