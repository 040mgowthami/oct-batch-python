user_name=input("enter your name: ")
user_password=input("enter your password: ")
inbuild_user_name="admin"
inbuild_user_password="admin123"

if user_name==inbuild_user_name and user_password==inbuild_user_password:
    print("login success")
else:
    print("invalid username or password")
