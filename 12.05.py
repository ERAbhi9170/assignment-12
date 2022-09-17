from itertools import count
num = 1

for m in count(num+1):
        
    for n in range(2, m):
        
        if(m % n == 0):
            
            break
    else:
        
        print('The Next prime number of {', num, '} is:', m)
        
        break