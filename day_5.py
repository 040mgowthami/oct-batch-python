# weight=(int(input("enter your weight: ")))
# height=int(input("enter your height: "))
# bmi=(weight/height**2)
# if bmi<18.5:
#     print("underweight")
# elif 25<=bmi<25:
#     print("overweight")
# elif bmi>=30:
#     print("obese")
# else:
#     print("valid number")

# unit=int(input("enter number of unit: "))
# if unit<=100:
#     bill=unit*1
# elif unit<=200:
#     bill=100*1+(unit-100)*2
# else:
#     bill=100*1+100*2+(unit-200)*5
# print(bill)

# a=int(input("enter a angle: "))
# b=int(input("enter second angle: "))
# c=int(input("enter a third angle: "))
# if a==b and a==c and b==c:
#     print("equil")
# elif a==b or b==c or a==c:
#     print("isoscel")
# else:
#     print("scalene")

# age=int(input("enter your age"))
# if age>=18:
#     print("allowed")
#     if age>=18 and age<30:
#         print("2$ ticket price")
#     elif age>=30 and age<60:
#         print("1$ ")

#         else:
#         print("0$ ")

# age=int(input("enter your age: "))
# if age>=18:
#     print("eligibal to swmming")
#     height=int(input("enter your height: "))
#     if height >=5:
#         print("pay $500 ")
#     else:
#         print("pay $600")
# else:
#     print("not allowed")

a=int(input("enter a number: "))
if a%2==0:
    print("yes")
    b=int(input("enter a number: "))
    if b%2==0:
        print("yes")
    else:
        print("not possibal")
else:
    print("not possibal")
