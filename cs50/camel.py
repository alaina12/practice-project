# Get the input from the user
camelcase = input("camelCase: ")

#print snakecase
print("snake_case: ",end="")

#loop through every letter
for letter in camelcase:
        #check if the letter is uppercase
        if letter.isupper(): 
            #print underscore and letter in lowercase
            print('_'+letter.lower(), end="")
        # otherwisw,print letter
        else:
            print(letter,end="")
        

#print space at the end
print()
