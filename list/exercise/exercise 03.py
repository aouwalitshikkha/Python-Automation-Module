# Access the index of a list
nums = [5, 15, 35, 8, 98]

# Output: 5 --- 1, 15-  2

for elem in nums:
    print(str(elem).zfill(2),'------', nums.index(elem))

