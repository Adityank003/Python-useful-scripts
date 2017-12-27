import os
import fnmatch



Path = 'C:/Users/adityan/Downloads'



pattern = '*.jpg'

 
for root, dirs, files in os.walk(Path):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
