#!/usr/bin/python3

print("Content-Type: text/html\n\n")
print()

import cgi

# get data from html form

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

# end html file    
def HTMLEnd():
    print('''
    </body>
    </html>
    ''')
    

def main():
    HTMLHeaders()

    print("<h2>This is finally working</h2>")
    HTMLEnd()


main()
    
