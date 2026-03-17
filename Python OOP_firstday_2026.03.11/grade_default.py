class Student:
    def __init__(self):
        self.id=26003
        self.name="Vignarathan"
    def setmarks(self):
        self.m1=56
        self.m2=74
        self.m3=62
    def calctotal(self):
        total=self.m1+self.m2+self.m3
        return total
    def calcaverage(self):
        average=self.calctotal()/3
        return average
    def getresult(self):
        ave=self.calcaverage()
        if(ave>=75):
            result='A'
        elif(ave>=65):
            result='B'
        elif(ave>=55):
            result='C'
        elif(ave>=45):
            result='S'
        else:
            result='F'
        return result
    
    def display(self):
        print("ID \t: "+str(self.id))
        print("Name \t: "+self.name)
        print("Marks m1 : "+str(self.m1))
        print("Marks m2 : "+str(self.m2))
        print("Marks m3 : "+str(self.m3))
        print("Total \t: "+str(self.calctotal()))
        print("Average : "+str(self.calcaverage()))
        print("Result \t: "+self.getresult())

stu1=Student()
stu1.setmarks()
stu1.display()
        
    