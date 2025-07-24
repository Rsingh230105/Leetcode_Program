import json
d={
    'course_name':'python',
    'fess':2000
}

f=json.dumps(d)
print(f)
print(type(f))