# def largest_prime_factor(n):
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 0
    # if n < 0:
    #     return 0
    # # Get list of prime numbers
    # a = list(range(int(n) + 1))
    # a[1] = 0
    # lst = []
    # i = 1
    # while i <= n:
    #     if a[i] != 0:
    #         lst.append(a[i])
    #         for j in range(i, n + 1, i):
    #             a[j] = 0
    #     i += 1
    #
    # lst.sort(reverse=True)
    # # Get largest prime factor of n
    # res = 1
    # for num in lst:
    #     if n % num == 0:
    #         res = num
    #         break
    #
    # return res
    #********************************


def largest_prime_factor(n):
    i = 2
    largest_prime = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i += 1

    if n > largest_prime:
        largest_prime = n

    return largest_prime

print(largest_prime_factor(17))

# **************************************


# Python3 code to find largest prime
# factor of number
import math


# A function to find largest prime factor
def maxPrimeFactors(n):
    # Initialize the maximum prime factor
    # variable with the lowest one
    maxPrime = -1

    # Print the number of 2s that divide n
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1  # equivalent to n /= 2

    # n must be odd at this point,
    # thus skip the even numbers and
    # iterate only for odd integers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n = n / i

            # This condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        maxPrime = n

    return int(maxPrime)


# Driver code to test above function
n = 15
print(maxPrimeFactors(n))

n = 25698751364526
print(maxPrimeFactors(n))












