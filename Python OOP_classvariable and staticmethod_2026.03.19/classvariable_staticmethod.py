class A:
    name="vignarathan" #class variable
    @staticmethod
    def getx(self):
        pass
        
class B(A):
    def __init__(self):
        self.x=10
    def getx(self):
        print("Bx is ",self.x)

objb=B()
print(objb.name)
print(A().name)