spam = 0
while spam < 5:
    print('Hello world!')
    spam = spam +1
    

name1 = ''
while name1 != 'Alex':
    print('Please, type your name.')
    name1 = input()
print('Thank you!')


name2 = ''
while True:
    print('Please, type your name.')
    name2 = input()
    if name2 != 'your name':
        break
print('Thank you!')


spam2 = 0
while spam2 < 5:
    spam2 = spam2 + 1
    if spam2 == 3:
        continue
    print('spam2 is ' + str(spam2))

