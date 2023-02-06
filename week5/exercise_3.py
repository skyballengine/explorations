import json

names_string = "William, Patrick, Jon, Tom, Peter, Colin, Sylvester, Paul, Chris, David, Matt, Peter, Jodie"
names_list = names_string.split(",")
stripped_names_list = [name.strip() for name in names_list]
names_dict = {index + 1: name for index, name in enumerate(stripped_names_list)}

with open('dict.json', 'w') as outfile:
    json.dump(names_dict, outfile)

with open('dict.json', 'r') as infile:
    new_dict2 = json.load(infile)
print(new_dict2)
