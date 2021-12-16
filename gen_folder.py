import os
import shutil

lis = os.listdir('./')

for l in lis:
    if 'bag' in l:
        name = l.split('.')[0]
        dir = os.getcwd()+'/'+name
        os.mkdir(dir)
        source = os.getcwd()+'/'+l
        dest = dir+'/'+l
        shutil.move(source, dest)