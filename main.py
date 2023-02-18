#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill = input( "What is the total bill? $")

percentage = input("what percentage of tip would you like to give? ")

split_bill = input("how many people to split the bill? ")

tip =  float(bill) / 100  * int(percentage) 

total_bill = float(bill) + tip

shared_bill = float(total_bill) / int(split_bill)

final_payment = round(shared_bill, 2)
print(f"Each person should pay: ${final_payment} ")