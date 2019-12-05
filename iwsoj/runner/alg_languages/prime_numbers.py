import sys
import math

def prime(n):
    if n < 2:
        return 0;
    else:
        counter = 0
        for i in range(2, (n+1)):
            counter = counter + 1
            for j in range(2, (math.floor(math.sqrt(i))+1)):
                if i % j == 0:
                    counter = counter - 1
                    break
        return counter

                
theInts = []
i = 0
for val in sys.stdin.read().split():
    theInts.append(int(val))
    print(prime(theInts[i]))
    i = i + 1