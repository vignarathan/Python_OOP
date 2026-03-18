from protected_modifier import A
from protected_modifier import B
from protected_modifier import C

#object for A
obja=A()
obja.getx()
print(obja.x)
print(obja._y) #output will come,because _y is protected so obja can access it

print("************************")
#B is sub class of A
objb=B()
objb.getx()
print(objb.x)
print(objb._y) # _y is protected so sub class can access it

print("************************")
#C has no connections with A,So object of C can't access anything from class A
'''objc=C()
print(objc.x)
objc.getx()
print(objc._y)'''

