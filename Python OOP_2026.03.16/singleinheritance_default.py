class A:
    def __init__(self):
        self.x=10
    def getx(self):
        print("Ax is "+str(self.x))
    
class B(A):
    def __init__(self):
        super().__init__()
        self.y=20
    def gety(self):
        print("By is "+str(self.y))

obj1=B()
obj1.getx()
obj1.gety()