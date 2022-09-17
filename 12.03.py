start = 1
end = 100
print('All prime numbers from 1 to 100')
for n in range(start, end+1):
    # all prime num grater than 1
    if n > 1:
        for i in range(2, n):
           if (n % i) == 0:
               break
        else:
           print(n, end=' ')