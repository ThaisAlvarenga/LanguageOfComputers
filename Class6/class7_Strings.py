# ASCII Tables are wheat allow you to manipulate characters for strings
# they are in decimal system and are then converted to binary



letter = "A"

# also prints a but lower case
print(chr(97))
# this converts the chr back to its number representation
print(ord('a'))


# Datatype is a class with special functions called methods (behavior) and properties (data)
# An object has data and behaviour that manipulates the data

# objects (unlike datatypes) use references that tell you were the information is
# located in memory.

# len is not a method of string because it doesn't go with the syntax string.len()

word = "NYUAD"

# this knows that word means the length  of word
# you can also use this for lists or files (file would be written one line at a time)
for letter in word:
    print(letter)

# strings have a negative and a positive index
# the negative index goes from right to left and starts at -1, the positive goes from left to right
# and starts at 0

# the indexes in a string are alway len(string) -1 

sent ="NYUAD"

sent[0]
# prints 'N'
sent[-1]
# prints 'D'
sent[1:4]
# prints 'YUA'
sent[::-1]
# prints 'DAUYN'

phrase.split(' ') # you can also define any char that you want to split at

# PYTHON always assumes you have unlimited memory


#in is a keywords that allows you to find something
print('p' in 'apple') # will print True
# there also exists the find() which finds a vllues in the string

string = "NYUAD cats are 100"
# string.count("cats") will count how many times cats is in the string/sentence

#BE CAREFUL WITH CASES
# find and in fins things with the same case.
# tou can do str.find("cats".upper)

# password.strip() removes all white space and \n
# there is also lstrip() and rstrip()


sentence1 = "NYUAD cats are cool"
sentence2 = sentence1.replace("cats", mouse) 
# which means replace cats with mouse



# lists are printed in brackets by default

# .appends() adds an element to the list


# say you want to get the number of words in a phrase
# you can use size = sent.count(' ') + 1
# or you can do wordlist = sent.split()
# size = len(wordlist)
