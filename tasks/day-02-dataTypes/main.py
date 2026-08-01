# Subscripting
print("Hello"[2-1])

# String
print("123546"+"332156")


#integer = whole number
print (123+321)



#large integers
print(123_233_123_123)

# float
print(1.215541)
# boolean
print(True)
print(False)


# Print out the 4 different data types
print(type("sdasd"))
print(type(123))
print(type(123.3))
print(type(True))

# Type Conversion
print(int(int("124")+float(1.20)))  #adding an int and a float equals a float but if I convert the result into an integer it cuts the .x part

# Make this line of code run without errors

# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " + str(len(input("Enter your name\n"))))


# BMI Calculator
height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi =weight/height**2

print(bmi)