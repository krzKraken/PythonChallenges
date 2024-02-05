#!/usr/bin/env python

print("Create a Quick List of Capitalized Cities")
cities = ["ecuador","colombia", "estados unidos"]

capitalized_cities = [ city.title() for city in cities]
print(capitalized_cities)


print("Create a quick list with squares number from 0 to 64")

squares = [i**2 for i in range(9)]
print(squares)


print("-------DICCIONARIOS----")
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
for name, score in scores.items():
    print(f"{name}: {score}")