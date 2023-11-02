print("Welcome to Starbucks at NYUAD!")
size = input("Choose the size of your macchiato: \n\t 1. Small \n\t 2. Medium \n\t 3. Grande \n\t 4. Venti \n")

print(size)

if( size == 1):
    print("Your SMALL Macchiato will be ready in 2 minutes")
elif( size == 2):
    print("Your MEDIUM Macchiato will be ready in 4 minutes")
elif( size == 3):
    print("Your GRANDE Macchiato will be ready in 6 minutes")
elif( size == 4):
    print("Your VENTI Macchiato will be ready in 8 minutes")

else:
    print("Invalid selection, please choose again.")
    print("Make sure you only write the number of your choice (ex. if you want a Venti, write 4)")
