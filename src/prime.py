### using for loop
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i) == 0:
            return False
    return True

### using while
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if (n % i) == 0:
            return False
        i += 1
    return True
    
for i in range(2, 100):
    if isPrime(i):
        print(i)