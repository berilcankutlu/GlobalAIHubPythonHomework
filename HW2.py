First_Name,Last_Name  = input("Enter your first and last name: ").split(" ")
Age = int(input("Enter your age: "))
Date_Of_Birth = input("Enter your date of birth: ")

users=[]
users.append([First_Name, Last_Name,Age,Date_Of_Birth])
i = 0
for i in users:
    print(i)
    if i[2] < 18:
        print("You can not go out because it is too dangerous")
    else:
        print("You can go out to the street.")
