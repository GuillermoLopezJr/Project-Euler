def fact(n):
    if (n == 1):
        return 1
    else:
        return n * fact(n-1)

def digitSum(n):

    digSum = 0
    while (n != 0):
        dig = n % 10
        digSum += dig
        n = n // 10

    return digSum

def main():
    print(digitSum(fact(100)))

main()
