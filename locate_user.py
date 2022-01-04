import os
os.system("date")
#os.system("ls -l")
user_name=input("Enter Username:")
user_file=os.system("cat /etc/password")
if user_name in user_file:
    print("User Exists")
else:
    print("User does not exists")

