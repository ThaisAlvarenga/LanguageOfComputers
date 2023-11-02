'''
Name:Thais Alvarenga
Date: 01/02/2023

Description: Determine what developmental stage a person is in based on their age
'''

grade = int(input("grade: "))

if( grade > 0) and (grade <= 59):
    print(grade, "Your grade is F")
    print(grade, "You are FAILING")
    
elif( grade > 59) and (grade <= 69):
    print(grade, "Your grade is D")
    
elif( grade > 69) and (grade <= 79):
    print(grade, "Your grade is C")
    
elif( grade > 79) and (grade <= 89):
    print(grade, "Your grade is B")
    print(grade, "Great grade!")
    
elif( grade > 89) and (grade <= 100):
    print(grade, "Your grade is A")
    print(grade, "Excellent work!")

else:
    print("Invalid input")
