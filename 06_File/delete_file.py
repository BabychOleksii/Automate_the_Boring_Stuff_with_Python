import os, shutil, send2trash

os.unlink(r'bacon.txt')
os.rmdir(r'D:\Projects\06_File_copy')
shutil.rmtree(r'D:\Projects\06_File_copy')

send2trash.send2trash(r'hello2.txt')
