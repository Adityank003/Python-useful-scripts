import os
import fnmatch


#configure path where you need to search
#Below path searches entire C drive
Path = 'C:/'


#Files with extention you need to find
pattern = '*.jpg'

 
for root, dirs, files in os.walk(Path):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
