import json

json_str = '{"name": "newming", "age": 24}'

student = json.loads(json_str)

print(type(student))   # <class 'dict'>
print(student)    # {'name': 'newming', 'age': 24}

list_str = '["d", "e"]'

print(type(json.loads(list_str)))
print(json.loads(list_str))

dict_py = [
    {'name': 'newming', 'age': 14},
    {'name': 'dema', 'age': 18}
]
print(type(dict_py))    # list

res = json.dumps(dict_py)
print(res)
