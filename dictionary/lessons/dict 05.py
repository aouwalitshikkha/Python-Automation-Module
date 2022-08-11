# car = {"brand": "Ford", "model": "Mustang", "year": 1964, 'color':'White'}
# car_dict = car.copy()
# car_dict = dict(car)
# print(car_dict)

ford = {"brand": "Ford", "model": "Mustang", "year": 1964, 'color':'White'}
toyota = {"brand": "toyota", "model": "Toya", "year": 1930, 'color':'Red'}

car = {
    'ford':ford,
    'toyota':toyota
}
print(car['ford']['model'])