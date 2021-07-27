#Welcome the user to the program
opening_message = "Welcome to the tip calculator!"

#Get the total bill amount.
#Convert the bill to a float number by wrapping the input with "float".
total_bill = float(input('What was the total bill for tonight? $' ))

#Create a variable for the tip, and convert that to an integer. 
tip_percentage = int(input('What percentage of a tip would you like to leave? 5, 10, 12, or 15? '))

#Create a variable for the amount of people splitting bill, then convert it to an integer.
people_to_split_bill = int(input('How many people are splitting the bill? '))

#Divide the tip percentage by 100, then multipy that by the total bill amount, and lastly add that to the total bill. 
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
print(bill_with_tip)