import json

input = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Adit"
    }
]'''

info = json.loads(input)
print('User Count : ', len(info))

for item in info:
    print('Name : ', item["name"])
    print('ID : ', item["id"])
    print('Attribute :', item["x"])