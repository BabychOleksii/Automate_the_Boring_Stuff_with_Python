helloFile = open(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

helloFile = open(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\hello.txt')
content2 = helloFile.readlines()
print(content2)
helloFile.close()

helloFile = open(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\hello2.txt', 'w')
helloFile.write('Hello!!!!\nI create this file.')
helloFile.close()

baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()
