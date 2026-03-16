class A:
    def __init__(self,x):
        self.x=x
    def getx(self):
        print("Ax is "+str(self.x))

class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def gety(self):
        print("By is "+str(self.y))

obj1=B(15,25)
obj1.getx()
obj1.gety()