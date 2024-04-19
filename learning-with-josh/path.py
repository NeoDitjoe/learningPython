from pathlib import Path

path = Path('money')

# path.mkdir() # create folder
# path.rmdir() # remove folder
# print(path.exists()) #checks 

#checks if the dir exists
isDir = path.exists()

# If dir exist we remove
# If dir does not exist we remove it
if isDir:
  path.rmdir()
else:
  path.mkdir()
  
  
# return all my files in the josh dir 
path2 = Path('learning-with-josh')

for item in path2.glob('*'):
  print(item)
  
print(" ")
# return all my global files and dir
path3 = Path()

for item in path3.glob('*'):
  print(item)
  