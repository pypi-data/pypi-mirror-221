class Value:
    """
    The base class
    very simple just a value all numbers, fractions, decimals will extend value
    """
    def __init__(self, value):
        self._value = value
    def get(self):
        """ Just a .get() method for subclasses and/or clean code"""
        return self._value

    def set(self,new):
        """ Just a .set() method for subclasses and/or clean code"""
        # Who Knows This might help
        old = self.get()
        self._value = new
        return old