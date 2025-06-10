import json

import math

def perfect():
    number = int(input("Enter a number: "))
    answer = 0

    for i in range(1, number):
        if number % i == 0:
            answer += i

    if answer == number:
        print("Its perfect")
    else:
        print("Its not perfect")

perfect()


def prime():
    m = int(input("Enter a number to check if prime or not: "))
    primy = 0

    for i in range(2, m):
        res= m % i

        if res== 0:
            print("Its not a prime")
            break
        else:
            print("Its a prime")
            break

prime()

77.95

77.243

