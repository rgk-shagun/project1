'''
papa_age=36
mummy_age=30
daughter_age=4
son_age=2
family_member=input("Enter Family member type e.g papa, mummy, daughter, son : ")
if family_member=="papa":
    print(f"Papa's age is {papa_age}")
if family_member=="mummy":
    print(f"mummy's age is {mummy_age}")
if family_member=="daughter":
    print(f"Daughter's age is {daughter_age}")
if family_member=="son":
    print(f"Son's age is {son_age}")
'''



'''
member_name=input("Enter Family Member Name: ")
member_age=input(f"Enter Famliy Member age:  ")
print(f"{member_name} age is {member_age}")
'''



family_member=['Parmod','Kirti','Yashika','Rishu']
member_name=input("Enter Member Name : ")
if member_name in family_member:
    print(f"{member_name} is our family member")
else:
    print(f"{member_name} is not belong to my family")
