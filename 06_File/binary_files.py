import shelve

shelfFile = shelve.open('mydata')
shelfFile['cities'] = ['Toronto', 'Calgary', 'Edmonton', 'Winnipeg']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cities'])
shelfFile.close()

shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
