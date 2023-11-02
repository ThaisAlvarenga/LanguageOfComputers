
#!/usr/bin/python3

import cgi

print("Content-Type: text/html \n\n")

print()



# always declare your data as a global variable
formData = cgi.FieldStorage()



def HTMLHeaders():
    
    print('''<!DOCTYPE html>

    <html>

    <head>
    <title> [Placeholder] </title>
    <link rel="stylesheet" type="text/css" href="main.css">
    </head>

    <body>

    ''')


def getFormsValues():

    print("<h1> Thank you! </h1>")
  


def HTMLEnd():

    print("</body> </html>")


# use this functions so that when you copy from a program to another, you won't
# have issues with the html
# you can also put them in a module to reuse it

HTMLHeaders()

getFormsValues()

HTMLEnd()
 
