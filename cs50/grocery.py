#Create an empty dictionary
grocery = {

} 

#loop forever
while True:
    try:
        #get the user input
        item  = input().casefold()
        #check if item is already in the dictionary 
        if item in grocery :
            #if it exits then add 1 to the count 
            grocery[item] +=1
        #otherwise , add the ite for the first time 
        else :
           grocery[item] = 1
            
    
    except EOFError:
        #print the dictonary in alphabetical order
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
        #stop the loop 
        break

