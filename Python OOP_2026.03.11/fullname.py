class Student:
    
    def __init__(self,fname,lname,id):
        self.fname=fname
        self.lname=lname
        self.id=id
        
    def getfullname(self):
        return self.fname+" "+self.lname
    
    def display(self):
        print("my name is : "+self.fname)
        print("my id is : "+str(self.id))
        print("my fullname : "+self.getfullname())

stu1=Student("Vignarathan","Sivalingam",250044)
stu1.display()