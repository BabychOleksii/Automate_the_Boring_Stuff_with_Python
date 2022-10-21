import re

message = 'Call me 415-555-1011 tomorrow, or 415-555-9876 to my office.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
ml = phoneNumRegex.findall(message)

print(mo)
print(mo.group())
print(ml)

