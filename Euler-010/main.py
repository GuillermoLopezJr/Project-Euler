#Answer: 142913828922

from math import sqrt

def sieve(limit):
    nums = [True for i in range(limit)]
    primes = []

    for i in range(2, int(sqrt(limit))+1):
        if (nums[i] == True):
            for j in range(i*i, limit, i):
                nums[j] = False

    for i in range(2, limit):
        if (nums[i] == True):
            primes.append(i)

    return primes

def main():
    print(sum(sieve(2000000)))

main()
