import re

beginsWithRegex = re.compile(r'^Hello')
mo = beginsWithRegex.search('Hello, world!')
print(mo)

mo2 = beginsWithRegex.search('Say Hello to the world.')
print(mo2)

# =========================================

endsWithRegex = re.compile(r'world!$')
mo3 = endsWithRegex.search('Hello, world!')
print(mo3)

mo4 = endsWithRegex.search('Say Hello to the world.')
print(mo4)

# =========================================

allDigitsRegex = re.compile(r'^Hello, world!$')
mo5 = allDigitsRegex.search('Hello, world!')
print(mo5)

mo6 = allDigitsRegex.search('Say Hello to the world.')
print(mo6)

allDigitsRegex2 = re.compile(r'^\d+$')
mo7 = allDigitsRegex2.search('123x56')
print(mo7)

# =========================================

atRegex = re.compile(r'.at')
mo8 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo8)

atRegex2 = re.compile(r'.{1,2}at')
mo9 = atRegex2.findall('The cat in the hat sat on the flat mat.')
print(mo9)

# =========================================

nameRegex = re.compile(r'First Name: (.*)\, Last Name: (.*)')
mo10 = nameRegex.findall('First Name: Alex, Last Name: Muller')
print(mo10)


server = '<To serve human> for dinner>.'
greedy = re.compile(r'<(.*)>')
nongreedy = re.compile(r'<(.*?)>')
mo11 = greedy.findall(server)
mo12 = nongreedy.findall(server)

print(mo11)
print(mo12)

# =========================================

prime = 'To serve. \nAnd to protect.'
prime2 = '''To serve.
And to protect.'''

dotStar = re.compile(r'.*')
dotStar2 = re.compile(r'.*', re.DOTALL)

print(dotStar.search(prime))
print(dotStar.search(prime2))

print(dotStar2.search(prime))
print(dotStar2.search(prime2))

# =========================================

vowelRegex = re.compile(r'[aeiou]', re.I)
slogan = 'Alex always wants to go to Alaska.'
print(vowelRegex.findall(slogan))
