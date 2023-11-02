'''
NAME: Thais Alvarenga
DATE: 30/01/2023

Description: Program ask user to input Celsius and converts input to Farenheit.
It also does the reverse, converts Farenheit to Celsius. 
'''
# CELSIUS TO FARENHEIT

# prompt user to input temperature in Celsius
myCelsius = float(input("Temperature in Celsius:"))
# print out value
print(myCelsius,"°C")

# get temperature in celcius by using the conversion formula C x 9/5 + 32
# where C is the temperature in celsius
fahrenheit = myCelsius * 9 / 5 +32

# print conversion
print(myCelsius,"°C is equal to", fahrenheit, "°F")

# separate
print()

# --------------------------------------------------------------

# FARENHEIT TO CELSIUS

# prompt user to input temperature in Farenheit
myFahrenheit = float(input("Temperature in Farenheit:"))
# print out value
print(myFahrenheit,"°F")

# get temperature in celcius by using the formula (F - 32) x 5/9
# where F is the temperature in fahrenheit

celsius = (myFahrenheit - 32) * 5 / 9

# print conversion
print(myFahrenheit,"°F is equal to", celsius, "°C")
