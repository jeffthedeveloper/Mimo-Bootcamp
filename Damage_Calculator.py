import math

from tabulate import tabulate

weapons = [["sword", 5], ["axe", 7], ["wand", 4]]
results = []
headers = ["Weapon", "Damage", "Power Attack"]

for weapon in weapons:
    name = weapon[0]
    damage = weapon[1]
    power_attack = math.pow(damage, 2)
    results.append([name, damage, power_attack])

output = tabulate(results, headers)
print(output)
