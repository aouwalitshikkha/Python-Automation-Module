# Print the numbers of a specified list after removing even numbers from it
num = [7,8, 120, 25, 44, 20, 27]

# option 1
new_list = []
for elem in num:
    if elem % 2 == 1:
        new_list.append(elem)
print(new_list)

# option 2
num = [x for x in num if x % 2 != 0 ]
print(num)

