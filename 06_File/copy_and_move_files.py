import shutil

shutil.copy('D:\\Projects\\Automate_the_Boring_Stuff_with_Python\\06_File\\hello.txt', 'D:\\Projects')
shutil.copy('D:\\Projects\\Automate_the_Boring_Stuff_with_Python\\06_File\\hello.txt', 'D:\\Projects\\hello3.txt')
shutil.copytree('D:\\Projects\\Automate_the_Boring_Stuff_with_Python\\06_File', 'D:\\Projects\\06_File_copy')
shutil.move('D:\\Projects\\06_File_copy\\hello2.txt', 'D:\\Projects\\')
shutil.move('D:\\Projects\\hello2.txt', 'D:\\Projects\\hello2_copy.txt')
