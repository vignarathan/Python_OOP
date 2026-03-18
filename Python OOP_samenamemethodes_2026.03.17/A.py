class A:
    def __init__(self):
        pass
    def getstudent(self,sid):   
        self.sid=sid           
        print("ID is "+str(self.sid))
    # def getstudent(self,name):
        # self.name=name
        # print("Name is "+str(self.name))
       
       
 '''two methods with same name and different parameter can in a python module
     but,when we call the method with different argument, only one will work'''
     #It's not like Overloading
           