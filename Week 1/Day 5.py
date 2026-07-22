# Q- Check whether a number is Armstrong or not

def is_armstrong(number):
    # Convert number to string to easily loop through digits and count them
    num_str = str(number)
    power = len(num_str)
    
    # Calculate the sum of digits raised to the power
    total_sum = sum(int(digit) ** power for digit in num_str)
    
    # Return True if it matches the original number, otherwise False
    return total_sum == number

# Test the function
test_num = 1634
if is_armstrong(test_num):
    print(f"{test_num} is an Armstrong number!")
else:
    print(f"{test_num} is NOT an Armstrong number.")


# Q - Find the maximum and minimum in a list.

# Define a list of numbers
numbers = [42, 17, 89, 5, 63, 22]

# Find extreme values using built-in methods
maximum_value = max(numbers)
minimum_value = min(numbers)

print(f"Maximum: {maximum_value}")  # Output: 89
print(f"Minimum: {minimum_value}")  # Output: 5

# Other method

def find_extremes(num_list):
    # Handle the edge case of an empty list safely
    if not num_list:
        return None, None
    
    # Initialize variables with the first element of the list
    max_val = num_list[0]
    min_val = num_list[0]
    
    # Loop through the list and update values dynamically
    for num in num_list:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    return max_val, min_val

# Test the function
numbers = [42, 17, 89, 5, 63, 22]
maximum, minimum = find_extremes(numbers)

print(f"Maximum: {maximum}")  # Output: 89
print(f"Minimum: {minimum}")  # Output: 5



