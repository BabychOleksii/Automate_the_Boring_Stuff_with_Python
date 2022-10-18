name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice!')
elif age < 12:
    print('You are a kid.')
elif age > 2000:
    print('You are too old')
elif age > 100:
    print('You are not Alice, grannie.')
    

print('Enter a name.')
name = input()
if name:
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')
