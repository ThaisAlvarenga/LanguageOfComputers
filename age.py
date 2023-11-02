'''
Name:Thais Alvarenga
Date: 01/02/2023

Description: Determine what developmental stage a person is in based on their age
'''

age = int(input("How old are you? "))

#print(age)

if (age > 0) and (age <= 2):
    print("You are a baby")
    
elif (age > 2) and (age <= 4):
    print("You are a toddler")
    
elif (age > 4) and (age <= 12):
    print("You are a child")
    
elif ( age > 12) and (age <= 25):
    print("You are a teenager")

elif (age < 25):
    print("You are an adult (i HOPE)")
    
# the last else satisfies all the non-true conditions
# leave this for all the strange data (the ones you don't have to check)
else:
    print("strange/invalid age")


# TIP: only concentrate on making case scenarios for valid data, not for things
# that could be invalid
