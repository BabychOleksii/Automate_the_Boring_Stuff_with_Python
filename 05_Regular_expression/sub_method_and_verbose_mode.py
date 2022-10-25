import re

message = 'Agent Jack gave some donuts to Agent Kevin.'

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall(message))
print(namesRegex.sub('REDACTED', message))

namesRegex2 = re.compile(r'Agent (\w)\w*')
print(namesRegex2.findall(message))
print(namesRegex2.sub(r'Agent \1***', message))

# =============================================

message = 'Call me tomorrow 415-555-9876#434 to my office.'
phoneNumRegex = re.compile(r'''
\d\d\d- # area code
\d\d\d- # first three digits
\d\d\d\d # last four digits
\#\d\d\d # internall connect code
''', re.VERBOSE)
print(phoneNumRegex.search(message))

# =============================================

prime = 'To serve. \nAnd to protect.'
multiCompile = re.compile(r'[aeiou]', re.DOTALL | re.I)
print(multiCompile.findall(prime))
