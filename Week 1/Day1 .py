# EASY QUESTIONS

# Q1 - Capitalize the word
s = 'hello world'
print(s.title())  # Hello World

# Q2 - remove spaces from word
s = "   Prakhar    "
print(s.strip())  # Prakhar

# Q3 - replace the wrod "awesome to great"
s = "python is awesome"
print(s.replace("awesome", "great"))  # python is great

# Q4- Check palindrome or not
palindrome = "racecar"
print(palindrome == palindrome[::-1])  # True

# Q5- reverse the order
s = "my name is prakhar"
print(" ".join(s.split()[::-1]))  # prakhar is name my

# MEDIUM QUESTIONS

# Q6 - Count "a" in "banana" without .count()

s = "banana"
count = 0
for char in s:
    if char == "a":
        count += 1
print(count)  # 3

# Q7 - "hello" → "h-e-l-l-o"

s = "hello"
print("-".join(s))  # h-e-l-l-o


# Q8 - Remove duplicates, maintain order

s = "aabbccdd"
seen = []
for char in s:
    if char not in seen:
        seen.append(char)
print("".join(seen))  # abcd


# Q9 - Extract numbers from string

s = "Price is 100 rupees and 200 paise"
numbers = []
for word in s.split():
    if word.isdigit():
        numbers.append(int(word))
print(numbers)  # [100, 200]


# Q10 - Anagram check

s1 = "Listen"
s2 = "Silent"
print(sorted(s1.lower()) == sorted(s2.lower()))  # True


# Q11 - String compression "aaabbbccca" → "a3b3c3a1"

s = "aaabbbccca"
result = ""
i = 0
while i < len(s):
    char = s[i]
    count = 1
    while i + count < len(s) and s[i + count] == char:
        count += 1
    result += char + str(count)
    i += count
print(result)  # a3b3c3a1


# Q12 - Longest substring without repeating chars

s = "abcabcbb"
left = 0
max_len = 0
best = ""
seen = {}

for right in range(len(s)):
    if s[right] in seen and seen[s[right]] >= left:
        left = seen[s[right]] + 1
    seen[s[right]] = right
    if right - left + 1 > max_len:
        max_len = right - left + 1
        best = s[left:right+1]

print(best, max_len)  # abc 3


# Q13 - Reverse words

s = "the sky is blue"
print(" ".join(s.split()[::-1]))  # blue is sky the


# Q14 - Balanced brackets

s = "({[]})"
stack = []
pairs = {")": "(", "}": "{", "]": "["}

for char in s:
    if char in "({[":
        stack.append(char)
    elif char in ")}]":
        if not stack or stack[-1] != pairs[char]:
            print(False)
            break
        stack.pop()
else:
    print(len(stack) == 0)  # True


# Q15 - Caesar Cipher shift by 3

s = "hello"
result = ""
for char in s:
    shifted = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
    result += shifted
print(result)  # khoor

# CHAPTER 2- Data type & Variable

# Q-1 Find Remainder when a number is divisible by z

n = 18
z = 5
print(n%z)

# Q-2 Check the type of variable assigned using input () function.

n = input("ENter number")
print(type(n))

# Q-3 Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

a = 34
b = 80

if a >b:
    print('a is greater than b')
else:
    print('not greater')

# Q-4 Write a python program to find an average of two numbers entered by the user.

n = int(input("Enter number 1: "))
n1 = int(input("ENter number 2: "))

Avg= (n + n1)/2
print(Avg)