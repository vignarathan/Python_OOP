class Student:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def setmarks(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
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

#get input from user        
na=input("Enter Name : ")
sid=input("Enter ID :")
g1=int(input("Enter Marks m1 :"))
g2=int(input("Enter Marks m2 :"))
g3=int(input("Enter Marks m3 :"))

# send the inputs into class
stu1=Student(sid,na)
stu1.setmarks(g1,g2,g3)
stu1.display()
        