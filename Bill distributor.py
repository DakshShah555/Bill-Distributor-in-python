print("__________TIP CALCULATOR__________")
a = float(input("Enter the amount of the bill: "))

print("Enter 1: To enter the percentage of the tip \nEnter 2: To enter the amount of the tip")
reply = int(input("Enter one of the above options: "))

if reply == 1:
    b = float(input("Enter the percentage of the tip you want to give: "))
    c = float(input("Enter the number of members:"))
   
    final = (a + (a * b / 100)) / c
    print("Total bill: " + str(final * c))
    print("Distribution of bill: " + str(final))
else:
    d = float(input("Enter the amount of the tip you want to give: "))
    c = float(input("Enter the number of members:"))
    final_1 = (a + d) / c
    print("Total bill: " + str(final_1 * c))
    print("Distribution of bill: " + str(final_1))
