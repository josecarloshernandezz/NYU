# NYU
input ("Please enter the number of coins:")
quarters = (float (input ("# of quarters:"))
dimes = (float (input ("# of dimes:"))
nickels = (float (input ("# of nickels:"))
pennies = (float (input ("# of pennies:"))
dollar = (quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1) /100
cents =  (quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1) % 100
print ("The total is", dollar, "dollars and", cents, "cents") 
                
             
