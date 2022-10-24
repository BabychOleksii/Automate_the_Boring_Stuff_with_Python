import re

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventure of Batman')
mo2 = batRegex.search('The adventure of Batwoman')
mo3 = batRegex.search('The adventure of Batwowoman')
print(mo1.group())
print(mo2.group())
print(mo3)

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneRegex.search('Call me 415-555-1011 tomorrow.')
mo5 = phoneRegex.search('Call me 555-1011 to the office.')
print(mo4.group())
print(mo5.group())

# ===================================

batRegex2 = re.compile(r'Bat(wo)*man')
mo6 = batRegex2.search('The adventure of Batman')
mo7 = batRegex2.search('The adventure of Batwowoman')
mo8 = batRegex2.search('The adventure of Batwowowowoman')
print(mo6.group())
print(mo7.group())
print(mo8.group())

# ===================================

batRegex3 = re.compile(r'Bat(wo)+man')
mo9 = batRegex3.search('The adventure of Batman')
mo10 = batRegex3.search('The adventure of Batwowoman')
mo11 = batRegex3.search('The adventure of Batwowowowoman')
print(mo9)
print(mo10.group())
print(mo11.group())

# ===================================

haRegex = re.compile(r'(Ha){3}')
mo12 = haRegex.search('He said "HaHa"')
mo13 = haRegex.search('He said "HaHaHa"')
mo14 = haRegex.search('He said "HaHaHaHaHa"')
print(mo12)
print(mo13.group())
print(mo14.group())

# ===================================

digitRegex = re.compile(r'(\d){3,5}')
mo15 = digitRegex.search('1234567890')
mo16 = digitRegex.search('98765stars123456')
print(mo15.group())
print(mo16.group())

# ===================================

digitRegex2 = re.compile(r'(\d){3,5}?')
mo17 = digitRegex2.search('98765stars123456')
print(mo17.group())
