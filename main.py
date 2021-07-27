#Welcome the user to the program
opening_message = "Welcome to the tip calculator!"
print(opening_message)
#Get the total bill amount.
#Convert the bill to a float number by wrapping the input with "float".
total_bill = float(input('What was the total bill for tonight? $' ))

#Create a variable for the tip, and convert that to an integer. 
tip_percentage = int(input('What percentage of a tip would you like to leave? 5, 10, 12, or 15? '))

#Create a variable for the amount of people splitting bill, then convert it to an integer.
people_to_split_bill = int(input('How many people are splitting the bill? '))

#Divide the tip percentage by 100, then multipy that by the total bill amount, and lastly add that to the total bill. 
bill_with_tip = tip_percentage / 100 * total_bill + total_bill
#To figure out how much every person needs to pay, we divide the total bill amount with tip included, by the amount of people splitting the bill
bill_per_person = bill_with_tip / people_to_split_bill
#Finally, we want to round the bill per person by 2 decimal points and save that to a variable
final_amount = round(bill_per_person, 2)
#The{:.2f} tells us that we want to show both numbers to the right of the decimal point (we want 2 decimal points in our float number) for ex. .90 instead of .9
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")