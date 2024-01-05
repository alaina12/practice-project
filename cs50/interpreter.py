#Get the user input
expression = input("Expression: ")

#covert the input into variable
x, y, z = expression.split(" ")

#change the type of x and z to float
new_x = float(x)
new_z = float(z)
#calculate the result
if y == '+':
 result = new_x + new_z
if y=='-':
 result = new_x - new_z
if y== '*':
 result = new_x * new_z
elif y == '/':
 result = new_x / new_z

print(result)