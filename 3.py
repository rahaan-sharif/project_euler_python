from math import sqrt

def is_prime(num):
    sqrt_num=int(sqrt(num))+1
    for i in range(2, sqrt_num):
        if num%i==0:
            return 0
    return 1

def prime_factors(num):
    sqrt_num=int(sqrt(num))+1
    for i in range(1, sqrt_num):
        if num%i==0:
            if is_prime(i):
                print(i)
            if is_prime(num/i):
                print(num/i)

in_num=int(input("enter your value: "))
prime_factors(in_num)