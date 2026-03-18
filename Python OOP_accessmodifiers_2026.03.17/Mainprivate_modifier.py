from private_modifier import A
from private_modifier import B
from private_modifier import C

#object for A
obja=A()
obja.getx()
print(obja.x)
# print(obja.__y) Error will come,because __y is private

print("************************")
#B is sub class of A
objb=B()
objb.getx()
print(objb.x)
#print(objb.__y) #Error will come,because __y is private

print("************************")
#C has no connections with A,So object of C can't access anything from class A
'''objc=C()
print(objc.x)
objc.getx()
print(objc.__y)'''




