import re

message = 'Call me 415-555-1011 tomorrow, or 415-555-9876 to my office.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
mo2 = phoneNumRegex.findall(message)
print(mo)
print(mo2)

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex2.findall(message)
print(mo3)

phoneNumRegex3 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
mo4 = phoneNumRegex3.findall(message)
print(mo4)

# =========================================================

lyrics = '''On the twelfth day of Christmas my true love sent to me:
12 Drummers Drumming, 11 Pipers Piping, 10 Lords a Leaping, 9 Ladies Dancing, 8 Maids a Milking, 7 Swans a Swimming,
6 Geese a Laying, 5 Golden Rings, 4 Calling Birds, 3 French Hens, 2 Turtle Doves and a Partridge in a Pear Tree'''

xmasRegex = re.compile(r'\d+\s\w+')
mo5 = xmasRegex.findall(lyrics)
print(mo5)

#===========================================================

message2 = 'The adventure of Batman.'

vowelRegex = re.compile(r'[aeiouAEIOU]')
atofRegex = re.compile(r'[a-f]')

mo6 = vowelRegex.findall(message2)
mo7 = atofRegex.findall(message2)
print(mo6)
print(mo7)

notvowelRegex = re.compile(r'[^aeiouAEIOU]')
mo8 = mo6 = notvowelRegex.findall(message2)
print(mo8)
