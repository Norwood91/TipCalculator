#Welcome the user to the program
opening_message = "Welcome to the tip calculator!"
print(opening_message)
#Get the total bill amount.
#Convert the bill to a float number by wrapping the input with "float".
total_bill = float(input('What was the total bill for tonight? $' ))
print(total_bill)
#Create a variable for the tip, and convert that to an integer. 
tip_percentage = int(input('What percentage of a tip would you like to leave? 5, 10, 12, or 15? '))
print(tip_percentage)