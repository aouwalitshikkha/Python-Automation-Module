car = {"brand": "Ford", "model": "Mustang", "year": 1964, 'color':'White'}

# accessing
print(car['brand'])
print(car.get('year'))

# Keys or Values
print(list(car.keys()))
print(list(car.values()))
print(car.items())

# Copy
car_data = car.copy()
car_data = dict(car)
