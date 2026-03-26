from abc import ABC,abstractmethod #abc:-abstract base class
class A(ABC):
    @abstractmethod
    def getx(self):
        pass
        
class B(A):
    def __init__(self):
        self.x=10
    def getx(self):
        print("Bx is ",self.x)

objb=B()
objb.getx()