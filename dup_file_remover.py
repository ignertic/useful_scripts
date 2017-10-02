#My duplicate file remover
#This script removes duplicates of files [*-Copy(%d)]
import time
import glob
import os

files = glob.glob('*.*')
del_fi = []
count = len(files)
raw_input('{} found'.format(len(files)))
while count > 0:
    for fil in files:
        count = count - 1
        if fil[-8:-4] == 'Copy' :
            print 'File {} has duplicate'.format(fil)
            del_fi.append(fil) 
            
        else:
            print 'Loop Continue'
        
print 'Done'
print 'To b deleted'
for i in del_fi:
    print i
raw_input('TO delete {} files'.format(len(del_fi)))
for i in del_fi:
    os.remove(i)
    print 'Deleted {}'.format(i)

raw_input('Done')
