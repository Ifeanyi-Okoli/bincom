""" 
write a recursive searching algorithm to search for a number entered by user in a list of numbers.
"""
import random
import statistics

# Generate a list of random numbers
numbers = [random.randint(0, 100) for _ in range(10)]
num_list = [num for num in range(100)]

#Get user input
target_num = int(input("Enter a number to search:   "))


def recursive_search(numbers, target):
    if not numbers:  # Base case: Empty list
        return False #f'Sorry! You entered an invalid number, {target}. Try again next time. Thank you'
    
    middle = len(numbers) // 2
    if numbers[middle] == target:  # Base case: Number found
        return True, f'Congratulations!, your number, {target} is found.'
    elif numbers[middle] < target:  # Recursive case: Number is in the right half
        return recursive_search(numbers[middle+1:], target)
    else:  # Recursive case: Number is in the left half
        return recursive_search(numbers[:middle], target)

print(recursive_search(num_list, target_num))