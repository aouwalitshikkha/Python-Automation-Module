"""
Write a Python program to print a specified list
after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#
# sample_list.pop()       # yellow will be removed
# sample_list.pop()       # pink will be removed
# sample_list.pop(0)       # Red will be removed
#
# print(sample_list)

# Option 2
sample_list = [x for (i,x) in enumerate(sample_list) if i not in (0,4,5)]
print(sample_list)






