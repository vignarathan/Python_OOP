#protected modifier
class A:
    def __init__(self):
        self.x=53
        self._y=47 #use _ for protected access modifier
    def getx(self):
        print("Ax is "+str(self.x))
        print("Ax is "+str(self._y))

#class B is sub class of A
class B(A):
    def __init__(self):
        super().__init__()
    def _getBAx(self): # if we use _ with method name it's a protected method
        print("BAx")

#C has no connections with A
class C:
    def __init__(self):
        pass
    def getCAx(self):
        pass