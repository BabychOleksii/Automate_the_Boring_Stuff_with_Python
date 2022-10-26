import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.txt'))
print(os.sep)

# ============================================================

print(os.getcwd())
os.chdir('d:\\Projects')
print(os.getcwd())
os.chdir(r'D:\Projects\Automate_the_Boring_Stuff_with_Python')
print(os.getcwd())
os.chdir('.\\06_File')
print(os.getcwd())

# ============================================================

print(os.path.abspath('spam.png'))
print(os.path.abspath('..\\..\\spam.png'))

print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\filenames_and_paths.py'))

print(os.path.relpath(r'D:\Projects\06_File\filenames_and_paths.py', r'D:\Projects'))
print(os.path.dirname(r'D:\Projects\06_File\filenames_and_paths.py'))

print(os.path.basename(r'D:\Projects\06_File\filenames_and_paths.py'))
print(os.path.basename(r'D:\Projects\06_File'))

# ============================================================

print(os.path.exists(r'D:\Projects\06_File\filenames_and_paths.py'))
print(os.path.exists(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\filenames_and_paths.py'))

print(os.path.isfile(r'D:\Projects\06_File\filenames_and_paths.py'))
print(os.path.isdir(r'D:\Projects\06_File'))
print(os.path.isfile(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File\filenames_and_paths.py'))

# ============================================================

print(os.path.getsize(r'D:\Projects\Automate_the_Boring_Stuff_with_Python\06_File'))
print(os.path.getsize(r'.\filenames_and_paths.py'))
print(os.listdir(r'D:\Projects\Automate_the_Boring_Stuff_with_Python'))

# ============================================================

# Small program to calculate the size of all the files inside the directory in bytes (integer).
totalSize = 0
directory = 'D:\\Projects\\Automate_the_Boring_Stuff_with_Python\\06_File'
for filename in os.listdir(directory):
    if not os.path.isfile(os.path.join(directory, filename)):
        continue
    # print(os.path.join(directory, filename))
    # print(os.path.getsize(os.path.join(directory, filename)))
    totalSize = totalSize + os.path.getsize(os.path.join(directory, filename))

print(totalSize)
