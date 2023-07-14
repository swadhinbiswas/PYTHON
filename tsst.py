def find_nearstprime(n):
    if n<=1:
        return 2
    prime=n
    found=False
    while not found:
        prime+=1
        for i in range(2,prime):
            if prime%i==0:
                break
        else:
            found=True
    return prime
n=int(input())

print(find_nearstprime(n))
