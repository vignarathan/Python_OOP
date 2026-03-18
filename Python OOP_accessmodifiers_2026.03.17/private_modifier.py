#private access modifier
class A:
    def __init__(self):
        self.x=77
        self.__y=88 #use __ for private access modifier
    def getx(self):
        print("Ax is "+str(self.x))
        print("Ax is "+str(self.__y))
        
#class B is sub class of A
class B(A):
    def __init__(self):
        super().__init__()
    def __getBAx(self): # if we use __ with method name it's a private method
        pass

#C has no connections with A
class C:
    def __init__(self):
        pass
    def getCAx(self):
        pass
        
        
        