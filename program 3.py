mar=input("Enter M if married and U if unmarried ")
age=int(input("Enter your age "))
gender=input("Enter M if you are a male or enter F if you are a female ")
grant=False
if (mar=="M"):
    grant=True
elif (mar=="U" and age>30 and gender=="M"):
    grant =True
elif (mar=="U" and age>25 and gender=="F"):
    grant=True
if (grant):
    print ("You are insured.")
else:
    print ("You are not insured")