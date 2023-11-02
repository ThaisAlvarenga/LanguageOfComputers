
for num in range(100):

    # you can combine (num % 3 == 0) and (num%5 == 0)
    if (num % 15 == 0):
        print("BuzzFizz")
    elif(num % 3 == 0):
        print("Buzz")
    elif(num % 5 == 0):
        print("Fizz")
    else:
        print(num)
