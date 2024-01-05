#get the user input
item = input(str("item: "))

#create a dictionary for fruits
fruits = {
    'apple':130,
    'avacado': 50,
    'banana':110,
    'cantaloupe':50,
    'grapefruit':60,
    'grapes':90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon':15,
    'lime':20,
    'nectarine':60,
    'orange':80,
    'peach':60,
    'pineapple':50,
    'pear':100,
    'strawberries':50,
    'plums':70,
    'sweet cherries':100,
    'tangerine': 50,
    'watermelon':80

}


#loop over each fruit
for key in fruits:
    if key in item.casefold():
        print("Calories: ",fruits[key])





