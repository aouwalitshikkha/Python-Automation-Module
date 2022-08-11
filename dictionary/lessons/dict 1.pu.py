# dictionary = { 'key':'value'}
# Duplicate key is not allowed
# Dictionary Value Changeable

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

# print(car['brand'])
# print(car.get('model'))
# print(car.keys())
# print(list(car.keys()))

car['year'] = 1985

print(car)
