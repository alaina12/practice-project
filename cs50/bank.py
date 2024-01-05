greetings = input(str("Greetings: "))

if greetings.casefold().startswith('hello'):
    print('$0')
elif greetings.casefold().startswith('h' ):
    print('$20')
else:
    print('$100')