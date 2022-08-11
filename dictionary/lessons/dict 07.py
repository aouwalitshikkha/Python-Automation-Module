# clear(), fromkeys(), pop(), popitem(), setdefault(), update()

car = {"brand": "Ford", "model": "Mustang", "year": 1964, 'color':'White'}
# Clear or remove items

# car.clear()
# car.pop('year')
# car.popitem()
# print(car)

# Update
# car['year'] = 1990
# car.update({'year':1988})

# Insert

# car['Seat'] = 20
# car.update({'stearing':'Left'})
# print(car)

# s = car.setdefault('seat',20)
#
# print(car)

x = ('key1', 'key2', 'key3')
y = (0,1,2)

dicts = dict.fromkeys(x)
print(dicts)


