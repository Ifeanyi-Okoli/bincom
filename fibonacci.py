""" 
Write a program to sum the first 50 fibonacci sequence.
"""

def fibonacciSum(n):
    for i in range(n):
        if i == 0:
            prev = 0
            curr = 1
        else:
            sum = prev + curr
            prev = curr
            curr = sum
    return sum
    
    
    
    
print(fibonacciSum(50))