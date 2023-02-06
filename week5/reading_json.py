import json

with open('SuperSquad.json', 'r') as infile:
    super_squad = json.load(infile)

print(super_squad)
