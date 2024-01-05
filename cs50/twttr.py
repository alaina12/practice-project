# get the user input 
answer = input(str("Input: "))

#print output
print("output: ",end='')

#check each letter in the input
for char in answer:
    #check if there are vowels 
    if not char.casefold() in ['a','e','i','o','u']:
        print(char , end='')
print()