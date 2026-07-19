# Coding Practice Questions (Set 1)

# Q- Reverse a string

str = [1,2,3,4,5]
print(str[::-1])  # [5, 4, 3, 2, 1]

#  Q-  Find the factorial of a number

import math

result = math.factorial(7)

print(result)


#  Q- Check whether a number is prime

def is_prime(n: int) -> bool:
    # 1. Handle edge cases
    if n <= 1:
        return False
    if n <= 3:
        return True
        
    # 2. Eliminate multiples of 2 and 3 quickly
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # 3. Check factors up to the square root using 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True


# Examples
print(is_prime(13))   # Returns True
print(is_prime(100))  # Returns False


#  Q - Find largest number in a list

#  Use Built-in function

def find_largest(lst): # Space complexity :- o(1)
    return max(lst) if lst else None # Time complexity:- o(n)

# Use manual approach

def find_largest_manual(lst):
    if not lst: return None
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


# Q- Count vowels in a string

#  Optimized approach: O(n) time using a generator expression.
def count_vowels(s):
    vowels = set("aeiouAEIOU") # Set lookup is O(1)
    return sum(1 for char in s if char in vowels)
