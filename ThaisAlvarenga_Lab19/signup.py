#!/usr/bin/python3.2


'''
NAME: Thais Alvarenga 
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: ]Retrieves input from a form and outputs an html file with that information
DATE: 06/03/2023
'''

import cgi
import cgitb
cgitb.enable()

# define headers for the output html file
def HTMLHeaders():
    print("Content-type: text/html\n")
    print('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Form1 Submitted</title>
        <link rel="stylesheet" type="text/css" href="../main.css">
    </head>
    <body>
    ''')

    
'''
def getvalues():

    # get values from form
    username = data["username"].value
    password = data["username"].value

    print("your username is: ", username)
    print("your password is: ", password)

    # contactinate value into the line
    line = username + ':' + password + "\n"

    #open file (we use a because we want to append, not write)
    fileDB = open("thaisDB.txt", "a")

    # write values into DB (writing data values into file)

    fileDB.write(line)
    fileDB.close()

    print("done, open file userdata to see data")
'''

# print success message for user
def showSuccessFormSubmit():

    print('''
    <div class="submittedPage">
    <h1>Thank you!</h1>
    <p>Your form was submitted success fully.</p>
    <br>
    <hr>
    ''')


# end html file    
def HTMLEnd():
    print('''
    </body>
    </html>
    ''')


HTMLHeaders()
data = cgi.FieldStorage()
showSuccessFormSubmit()

HTMLEnd()
