from .Value import Value
from .Integer import Integer
from .Decimal import Decimal

class Number(Value):
    """
    If yur lazy or dont know if its whole or not use this helper
    """
    def __init__(self, value):
        if(type(value) == float):
            super().__init__(value)
            self._undervalue = Decimal(value)
        if(type(value) == int):
            super().__init__(value)
            self._undervalue = Integer(value)
    
    def get(self):
        return self._undervalue.get()
    def set(self, new):
        return self._undervalue.set(new)