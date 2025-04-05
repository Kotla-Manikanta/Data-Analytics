import json

#json to py
x='{"name":"kmk","age":35}'
z=json.loads(x)
print(z["name"])
print(z["age"])

#py to json
a={"name":"kmk","age":35}
b=json.dumps(a)
print(b)