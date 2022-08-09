# 'count’ , len  usage
str1 = "Python is awesome, isn't it?"

# Count the length

print('The Total character count is ',len(str1))

# Count Method
substring = 'awesome'
print("the Substring '",substring," present ",str1.count(substring), 'times')

substring2 = 'i'
print(str1.count(substring2,8,20))

# string.count(substring) ---- Return Total count
# string.count(substring, start, end) ---- Return Total count between start and end


