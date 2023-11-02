
# rectangle
for rows in range(5):
    for cols in range(10):
        print('#', end='')
    print()

print()

# square
for rows in range(1,6):
    for cols in range(rows):
        print('#', end='')
    print()

print()

# inverted triangles 
for rows in range(1,6):

    for cols in range(6-rows):
        print('', end='')
    for colrs in range (rows):
        print('*', end='')

print()

print()

# pattern in class

# rectangle
for rows in range(2):
    for cols in range(14):
        print('%', end='')
    print()
    
print()

# eyes
for rows in range(4):
    for cols in range(2):
        for colLine in range(3):
            print(' ', end="")
        for colLine2 in range(3):
            
            print('*', end="")
    print()

print()

# rectangle
for rows in range(2):
    for cols in range(14):
        print('%', end='')
    print()
    
print()
