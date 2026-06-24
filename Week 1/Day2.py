# LIST & TUPLES


# Q-1 Write a program to store seven fruits in a list entered by the user.

fruits = []
for i in range(7):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)
print(fruits)

# Q-2 Write a program to accept marks of 6 students and display them in a sorted manner.

marks_list = []

for i in range(6):
    mark = int(input("Enter marks: "))
    marks_list.append(mark)  # Make sure you are appending 'mark', NOT 'marks_list'

marks_list.sort()
print(marks_list)

# Q-3 Check that a tuple type cannot be changed in python.

marks_tuple = (34, 45, 6, 78, 990, 9)

try:
    
    marks_tuple[0] = 100 # type: ignore
except TypeError as error:
    
    print(f"Error caught successfully: {error}")


# Q-4 Write a program to sum a list with 4 numbers.


numbers = [10, 20, 30, 40]

total_sum = sum(numbers)

print("The list of numbers is:", numbers)
print("The sum of the list is:", total_sum)


# Q-5 Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

print(a.count(0))

