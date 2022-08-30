import math
sum=int(0)
for i in range(1,10):
    print(i,'的阶乘',math.factorial(i))
    sum+=math.factorial(i)
    print(i,'累积阶乘',hex(int(sum)))
