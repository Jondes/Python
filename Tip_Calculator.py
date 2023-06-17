name = input("What was the name of the resturant that you visited? ") #Ask user for resturant name.
meal = input("What was the value of your meal excluding taxes £ " ) #Ask user for value of meal w/o taxes.
tax = input("What is the Tax in your location? ") #Ask user for value of tax in their area.
totalwtax = float(meal) + float(tax) #Calculate total value of meal with tax.
tip = input("How was the service on a scale of 1 to 5? ") #Ask for level of service.

value = float(tip)

if value == float(1) or value == float(2): #If serivce was within 1 & 2
    print (float(totalwtax) + float(meal) * 0.05)
if value >= float(3) and value <= float (5): #If service was within 3 & 5
        print (float(totalwtax) + float(meal) * 0.08)
else:
    print ("Thank you! ")