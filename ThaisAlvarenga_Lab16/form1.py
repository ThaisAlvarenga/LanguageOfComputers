#!/usr/bin/python3

'''
NAME: Thais Alvarenga 
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: ]Retrieves input from a form and outputs an html file with that information
DATE: 06/03/2023
'''

import cgi

print("Content-Type: text/html \n\n")

print()

# get data from html form
formData = cgi.FieldStorage()

# define headers for the output html file
def HTMLHeaders():
    print('''

    <!DOCTYPE html>

    <html>

    <head>
    <title>Form1 Submitted</title>
    <link rel="stylesheet" type="text/css" href="main.css">
    </head>

    <body>

    ''')

# function to get the value of a form input using its key
def getFormsValues(valueKey):

    return formData[valueKey].value


# print success message for user
def showSuccessFormSubmit():

    print('''
    <div class="submittedPage">
    <h1>Thank you!</h1>
    <p>Your form was submitted success fully.</p>
    <p>Please double check your information before you leave this page.</p>
    <p>If there are any issues with your information, please email our alias. </p>
    <br>
    <hr>
    ''')

# display the information retrieved from form
def showFormInfo():
    print('<p> Name: ', name, '<p>')
    print('<p> Age: ', age, '<p>')
    print('</div>')

    
# end html file    
def HTMLEnd():
    print('''
    </body>
    </html>
    ''')




HTMLHeaders()

name = getFormsValues('fname')
age = getFormsValues('age')

showSuccessFormSubmit()

showFormInfo()

HTMLEnd()
