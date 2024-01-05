def main():
    # Get the time from the user
    user_time = (input("What time is it?"))
    #call the convert function
    time = convert(user_time)
    #breakfast between 7:00 to 8:00 
    if time >=7 and time<=8:
        print("Breakfast time")

    #lunch between 12:00 to 13:00
    if time >=12 and time <= 13:
        print("Lunch time")

    #dinner between 18:00 to 19:00
    if time >=18 and time <=19:
        print("Dinner time")


def convert(time):
    # Get the hour and minute
    hours,minutes = time.split(':')
    #convert time into float number
    new_minute = float(minutes)/60

    #return result to the main function
    return float(hours) + new_minute
if __name__=='__main__':
    main()
