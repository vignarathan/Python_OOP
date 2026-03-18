from A import A 
class B(A):
    def __init__(self):
        super().__init__()
        self.x=2222
        self.y=3333
    def getx(self):
        print("Bx is "+str(self.x)) #2222
        # ?? print("Ax is "+str(super().x))
        
    def gety(self):
        print("By is "+str(self.y)) #3333
        super().getx() #2222
        