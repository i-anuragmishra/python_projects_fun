import random
import time
t = time.time()
n = random.randint(1, 50000)
for i in range(1, n):
    if(i > 345):
        print(time.time()-t)
