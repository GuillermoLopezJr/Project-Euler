from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n))):
        if (n % i == 0):
            return False
    return True

def main():
    total = 0 
    for i in range(2, 10):
        if (isPrime(i)): 
            total += i
    print(total)
main()
