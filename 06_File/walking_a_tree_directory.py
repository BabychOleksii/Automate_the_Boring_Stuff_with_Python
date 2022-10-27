import os


for folderName, subfolders, filenames in os.walk(r'D:\Projects\Automate_the_Boring_Stuff_with_Python'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

