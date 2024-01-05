#while forever 
while True:
    #get the user input
    fuel = input("Fraction: ")
    try:
        #try to split the fuel
        numerator,denominator = fuel.split("/")
        #convert into integer
        new_numerator = int(numerator)
        new_denominator = int(denominator)
        #calculate the percentage
        f = new_numerator / new_denominator
        #check if its less than 1 and stop the loop
        if f<=1:
            break 
    except(ValueError , ZeroDivisionError):
        pass
#multiply percentage by 100
p = f * 100
#check if percentage is less than 1, print E
if p <= 1:
    print("E")
#chcek if percenatge is greater than 99, print F
elif p >= 99:
    print("F")
#otherwise, print the %
print(f'{p}%')