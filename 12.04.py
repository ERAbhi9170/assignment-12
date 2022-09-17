a = int(input("Enter the value of a : "))  
b = int(input("Enter the value of b : "))  

for k in range(a,b+1):
    for i in range(2,k+1):
        if k==i:
            print(k) 
        elif k%i!=0:
            continue
        else: 
            break