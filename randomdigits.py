""" 
Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
"""
import random

# Generate a list of random numbers
numbers = [random.randint(0, 1) for _ in range(4)]
print(numbers)

def binaryToDecimal(num):
    decimal = 0
    for bit in num:
        decimal = decimal*2 + int(bit)
    return decimal

print(binaryToDecimal(numbers))