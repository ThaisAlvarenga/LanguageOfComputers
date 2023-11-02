'''
Name: Thais Alvarenga

Date: 1/30/2023

Reversing digits of a 4 digit number

'''

# 1. enter a 4 digit number
num = int(input("Input a 4 digit year: "))
print(num)

# assuming the
# d1 d2 d3 d4

# 2. separate digit 1 and print it
d1 = num // 1000
print("D1: ",d1)

# 3. separate digit 2 and print it
d2 = num // 100 % 10
print("D2", d2)

# 4. separate digit 3 and print it
d3 = num % 100 // 10
print("D3", d3)

# 5. separate digit 4 and print
d4 = num % 10
print("D4:", d4)


# print reverse digits
print(str(d4)+str(d3)+str(d2)+str(d1))

# print("The number reversed is:")
