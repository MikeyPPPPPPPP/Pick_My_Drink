import json
import random

drink = []

with open('drinks.json','r', encoding='utf-8') as a:
    s = json.load(a)
    for x in s['alcohal']:
        drink.append(x)

r = random.randint(0,len(drink))

print(drink[r])
