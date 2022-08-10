languages = ['Python', 'C++', 'JavaScript', 'Java', 'Go', 'asp']
num_list = [1,5,2,8,3,4,6,7]

# programming_languages = languages.copy()
# del languages
# languages.extend(num_list)
# print(languages)

# Sort
# num_list.sort(reverse=True)

# num_list.reverse()
# print(num_list)

languages.sort(key=str.lower)
print(languages)





