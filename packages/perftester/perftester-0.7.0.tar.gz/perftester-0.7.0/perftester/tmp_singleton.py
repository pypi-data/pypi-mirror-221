from _collections_abc import Iterable
from collections import UserList

class Zupa(UserList):
    _instance = None

    def __new__(cls, data, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, data):
        super().__init__(data)
    
    def __add__(self, other: Iterable):
        raise NotImplementedError
    
    __radd__ = __add__
    __iadd__ = __add__
    
    def __mul__(self, value):
        raise NotImplementedError
    
    __imul__ = __mul__
    __rmul__ = __mul__
    
    def __setitem__(self, *args, **kwargs):
        raise ValueError
    

z = Zupa([10])
z += [20]
z *= 2
z[0] = 10

