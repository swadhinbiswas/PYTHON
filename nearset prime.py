def find_nearstprime(n):
    if n==1:
        return 2
    elif n>2:
        for i in range(2,n+1):
            if n%i==0:
             break
         
            
    return n

n=int(input())

print(find_nearstprime(n))
