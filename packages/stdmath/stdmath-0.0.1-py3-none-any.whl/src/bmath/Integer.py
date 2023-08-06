from .Value import Value

class Integer(Value):
    """
    A Integer Pretty Basic
    """
    def __init__(self, value):
        if(type(value) == int):
            super().__init__(value)
        else:
            raise RuntimeError("Integer not Provided. Please Provide  Proper Integer")