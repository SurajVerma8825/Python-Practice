username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "pass":
    print("You have successfully logged in")
elif username != "admin":
    print("You have entered wrong input")
else:
    print("Wrong password")
