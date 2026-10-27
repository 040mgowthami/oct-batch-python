password=input("enter your password: ")
alpha=""
digit=""
special=""
for ch in password:
    if ch.isalpha():
        alpha+=ch
    elif ch.digit:
        digit+=ch
    elif ch.special():
        special+=ch
    else:
        special+=ch
if len(digit)==2 and len(special)==1 and len(alpha)>3


