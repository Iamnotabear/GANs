import os
import glob
files = glob.iglob('./*')
i=0
for file in files:
    os.rename(file, '{}.jpg'.format(i))
    i=i+1
