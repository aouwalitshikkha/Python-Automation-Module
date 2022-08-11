# Accessing Tuple
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#              0        1       2           3       4       5          6
# Negative      -7      -6      -5          -4      -3      -2          -1

print(fruits[2])
print(fruits[-2])

print(fruits[1:4])      # 1,2 & 3
print(fruits[-4:-1])      #

if "banana" in fruits:
    print('Exists')
else:
    print('Sorry')



