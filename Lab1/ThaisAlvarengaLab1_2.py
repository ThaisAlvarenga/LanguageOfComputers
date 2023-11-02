'''
NAME: Thais Alvarenga
DATE: 30/01/2023

Description: Program that creates a spontaneous funny story (MAD LIBS) based on
the user's input of adjectives and nouns.
'''

# get adjective inputs from user
adjective = input("Write an adjective: ")
feeling = input("Give me a feeling: ")

# print adjectives
print("My adjective: ", adjective)
print("My feeling: ", feeling)

# leave a space
print()

# get noun inputs from user
city = input("Name a city: ")
animal = input("Name an animal: ")

# print nouns
print("My city: ", city)
print("My animal: ", animal)

# leave a space
print()
print("---------------------------------")
print()

# explain that next part is the mad lib
print("\tHere is your mad lib output:")
print()

# print mad lib with user inputs
print("One beautiful day, a little girl was walking through the streets of ", city + ".")
print("As she walked, she saw a", adjective ,animal + ".")
print("The girl was overtaken by a feeling of", feeling + ".")
print("But it didn't last long, so she kept walking.")
print("The End")
