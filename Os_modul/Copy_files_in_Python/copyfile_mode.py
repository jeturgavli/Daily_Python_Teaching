# copyfile = copies contents of a file
# copy()   = copyfile() + permission mode + destination can be a directory
# copy2()  = copy() + copies metadata (file's creation modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src.dst
shutil.copy('test.txt','copy2.txt') #src.dst
shutil.copy2('test.txt','copy3.txt') #src.dst
