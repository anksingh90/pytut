import json
data = {'name': 'Bob', 'age': 25, 'city': 'London'}
json_string = json.dumps(data)
print(json_string) # Output: { "name": "Bob", "age": 25, "city": "London" }
