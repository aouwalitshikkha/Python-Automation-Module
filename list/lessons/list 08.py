programing_language = ['python', 'c++', 'JavaScript']
num_list = [1,2,3,4,5,6,7,8,9,10]

# new_list = []
# for elem in programing_language:
#     newlist.append(elem.upper())

# new_list = [elem.upper() for elem in programing_language]

new_list = [x for x in num_list if x%2 == 1]

print(new_list)

# new_list = [expression for x in (list/set/tuple) if condition == true ]


