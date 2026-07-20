# Q -  Count vowels in a string.

# 1. Define the text string correctly
text = "Prakhar GUpta"

# 2. Convert everything to lowercase to catch "U" and "u"
text_lower = text.lower()

# 3. Count each vowel and add them up
vowels = "aeiou"
count = 0

for char in text_lower:
    if char in vowels:
        count += 1

print(count)  # Output: 4

# Other Method 

text = "Prakhar GUpta"
count = sum(1 for char in text.lower() if char in "aeiou")
print(count)  # Output: 4


# Q -  Find duplicate elements in a list.

def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
            
    return list(duplicates)

# Example usage:
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 1]
print(find_duplicates(my_list))  # Output: [1, 2]


# Other method 

my_list = [1, 2, 3, 2, 4, 5, 1, 6, 1]

# Find unique duplicates
duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))

print(duplicates)  # Output: [1, 2]


# Q - Check whether a string is a palindrome

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Example usage:
print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
print(is_palindrome("race a car"))  # Output: False
