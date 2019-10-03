import json

mary = {
    "name": "mary",
    "age": 17,
    "height": 5
}

with open("data.json", 'w') as f:
    json.dump(mary, f)

# with open("data.json", 'r') as f:
#     data = json.load(f)

# print(data)
# print(type(data))

# data["name"] = "marhooha"

# with open("data.json", 'w') as f:
#     json.dump(data, f)
