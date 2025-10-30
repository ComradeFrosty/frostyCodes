def nth_prime(n):
    count, num = 0, 1
    while count < n:
        num = num + 1
        if prime(num):
            count = count + 1
    return num

def prime (n):
    Flag = True
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            Flag = False
            break
    return Flag
