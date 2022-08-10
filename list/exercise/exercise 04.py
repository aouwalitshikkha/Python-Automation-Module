# Write a Python program to extend a list without append
# Sample data: [10, 20, 30] [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
# Sort it descend

list1 = [10, 20, 30]
list2 = [40, 50, 60]

list2.extend(list1)
print(list2)
list2.sort(reverse=True)
print(list2)




