# Q - Write rotate in array by K places
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(nums)
rotations = k%n
for i in range(0, rotations):
    e = nums.pop()
    nums.insert(0, e)


