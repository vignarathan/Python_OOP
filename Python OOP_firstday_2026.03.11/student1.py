class Student1:
    
    def __init__(self,name,id): #magic method
        self.name=name
        self.id=id
        
    def display(self): #instance method
        print("my name is "+self.name)
        print("my id is "+str(self.id))
    
stu1=Student1("Vignarathan",250044)
stu1.display()

stu2=Student1("Kayalnilavan",250045)
stu2.display()