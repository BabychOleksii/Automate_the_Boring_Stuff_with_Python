import re

message = 'My phone number is 415-555-1011.'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex.search(message)

print(mo.group())
print(mo.group(1))
print(mo.group(2))

# =================================

message2 = 'My phone number is (415) 555-1011.'
phoneNumRegex2 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumRegex2.search(message2)

print(mo2.group())

# =================================

message3 = 'Batman lost the wheel from the Batmobile and ride on the Batmotocycle.'

batRegex = re.compile(r'Bat(man|mobile|copter)')
mo3 = batRegex.search(message3)
mo4 = batRegex.findall(message3)

print(mo3.group())
print(mo3.group(1))
print(mo4)
