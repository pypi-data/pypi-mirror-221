from .Value import Value

class Decimal(Value):
    """
    A Decimal Pretty Basic
    """
    def __init__(self, value):
        if(type(value) == float):
            super().__init__(value)
        else:
            raise RuntimeError("Decimal not Provided. Please Provide  Proper Decimal")