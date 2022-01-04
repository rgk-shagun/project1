'''
import os
path=input("Enter your Dir Path : ")
if os.path.isfile(path):
    print(f" Don't enter file path")
else:
    file_dir=os.listdir(path)
    if len(file_dir)==0:
     print("Dir is Empty")
    else: 
      extension=input("Enter file extension e.g. .txt, .sh, .py etc. :")
      for extn in file_dir:
          if extn.endswith(extension):
'''
import os
dir_path=input("Enter Dir Path: ")
if os.path.exists(dir_path):
    dir_out=os.listdir(dir_path)
    if len(dir_out)==0:
     print("Dir is EMPTY")
    else:
     enter_extension=input("Enter file extension:")
     for file_ext in dir_out:
         if file_ext.endswith(enter_extension):
             print(file_ext)
         else:
             print("File extension does not exists")
else:
    print("Dir Not Exist")
#enter_extension=input("Enter file extension:")
