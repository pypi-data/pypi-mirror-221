from .Operation import Operation
from .Value import Value
from .Number import Number

class Multiply(Operation):
    def evaluate(self):
        if(type(self.value1) == Value):
            val1 = self.value1.get()
        elif(type(self.value1) == Operation):
            val1 = self.value1.evaluate().get()
        else:
            raise RuntimeError("Value 1 must be either a Value Or Operation")

        if(type(self.value2) == Value):
            val2 = self.value2.get()
        elif(type(self.value2) == Operation):
            val2 = self.value2.evaluate().get()
        else:
            raise RuntimeError("Value 2 must be either a Value Or Operation")
        return Number(val1 * val2)
        