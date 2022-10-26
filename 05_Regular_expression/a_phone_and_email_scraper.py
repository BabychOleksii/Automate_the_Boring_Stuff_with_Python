#! python3

import re, pyperclip

text = '''Contacts
DirectoryA-Z Directory U of T Experts - Blue Book Student Campus Organizations
St. George Campus 

General

University of Toronto
27 King's College Circle
Toronto, Ontario M5S 1A1 Canada

 Campus Maps
 www.utoronto.ca
 416-978-2011
 On Campus: Dial 1000
 Snow Line: 416-978-7669
Admissions

Undergraduate
 416-978-2190
 Ask a question
 Tours
 Apply to U of T
 
Graduate
 416-978-6614
 admissions.sgs@utoronto.ca
 School of Graduate Studies
Emergency

For emergencies:
 911 then Campus Safety 416-978-2222
For all other building related issues:
 416-978-3000
For IT system outages:
 joint operations group or 416-978-4621
 Additional emergency contacts
 Sexual Violence: Need help?
Mississauga Campus (UTM)

General

University of Toronto Mississauga
3359 Mississauga Road
Mississauga, Ontario L5L 1C6 Canada
general.sgs@utoronto.ca

 Campus Maps
 www.utm.utoronto.ca
 905-569-4455
Admissions

 905-828-5400
 Ask a question
 Tours
 Prospective Students
Emergency

For emergencies:
 911 then Campus Safety 905-569-4333
For all other building related issues:
 905-828-5200
For IT system outages:
 help desk or 905-828-5344
 Additional emergency contacts
 Sexual Violence: Need help?
Scarborough Campus (UTSC)

General

University of Toronto Scarborough
1265 Military Trail
Toronto, Ontario M1C 1A4 Canada

 Campus Maps
 www.utsc.utoronto.ca
 416-287-8872
Admissions

 416-287-7529
 Ask a question
 Tours
 Admissions
Emergency

For emergencies:
 911 then Campus Safety 416-978-2222
For all other building related issues:
 416-287-7579
For IT system outages:
 help desk or 416-287-4357
 Additional emergency contacts
 Sexual Violence: Need help?'''

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 123-123-1234, 123-1234, (123) 123-1234, 123-1234 ext 12345, ext. 12345, x12345    
(
((\d\d\d) |  (\(\d\d\d\)))?     # area code (optional)
(\s|-)                          # first separator
\d\d\d                          # first 3 digits
-                               # separator
\d\d\d\d                        # last 4 digits
(((ext(\.)?\s) | x)             # extension word-part (optional)
 (\d{2,5}))?                    # extension number-part (optional)
)
''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5})?.com

[a-zA-Z0-9_.+]+ #namepart
@               # @ symbol
[a-zA-Z0-9_.+]+  #domain name part
''', re.VERBOSE)

# Get the text off the clipboard
# text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# print(allPhoneNumbers)
# print(extractedEmail)

# Copy the extracted email/phone to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

print(results)
