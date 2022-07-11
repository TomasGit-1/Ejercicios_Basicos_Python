from array import *

arrayName = array('i' , [10 , 20 ,30 ,40 ,50 ,60 ,70 ,80])

for x in arrayName:
    print(x)

print('--------------------------------')

arrayName.insert(1, 90)
for x in arrayName:
    print(x)


print('--------------------------------')

arrayName.remove(90)
for x in arrayName:
    print(x)

