import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New york city': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    uName = input('please enter your name : ')
    print (f"Hello {uName}, I'm here to help you filter this data")
    print("Let's explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input(" please choose a city name like that (Chicago, New york city, Washington) : ").capitalize()
    while city not in CITY_DATA.keys():
        print("please choose one among allowed cities (Chicago, New york city, Washington) : ")
        city = input(" please choose a city name like that (Chicago, New york city, Washington) : ").capitalize()


    # get user input for month (all, january, february, ... , june)
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "All"]
    while True :
        month = input("please choose among allowed options :(Jan, Feb, Mar, Apr, May, Jun, All) : ").capitalize()
        if month in months :
            break
        else :
            print("please choose one among allowed options :(Jan, Feb, Mar, Apr, May, Jun, All) : ")
            month = input("please choose among allowed options :(Jan, Feb, Mar, Apr, May, Jun, All) : ").capitalize()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    DayInWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "All"]
    while True :
        day = input("please choose among allowed options :(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All) : ").capitalize()
        if day in DayInWeek :
            break
        else :
            print("please choose one among allowed options :(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All) : ")
            day = input("please choose among allowed options :(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All) : ").capitalize()



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["DayOfWeek"] = df["Start Time"].dt.day_name()
    df["StartHour"] = df["Start Time"].dt.hour
    
    if month != "All" :
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        month = months.index(month) +1

        df = df[df["Month"] == month]

        
    if day != "All" :
        DayInWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        df = df[df["DayOfWeek"] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df["Month"].mode()[0]
    print (f"The most common month is : ", df["Month"].mode()[0])

    # display the most common day of week
    day = df["DayOfWeek"].mode()[0]
    print (f"The most common day of week is : {day}")

    # display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    df["hour"].mode()[0]
    print (f"The most common Start Hour is : " , df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print ("The most commonly used start station is : {}".format(df["Start Station"].mode()[0]))

    # display most commonly used end station
    print ("The most commonly used end station is : {}".format(df["End Station"].mode()[0]))

    # display most frequent combination of start station and end station trip
    df["route"]=df["Start Station"] + "," + df["End Station"]
    print ("The most frequent combination of start station and end station trip is : {}".format(df["route"].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print ("Total travel time : ",(df["Trip Duration"]).sum())

    # display mean travel time
    print ("Mean travel time : ",(df["Trip Duration"]).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city) :
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print (df["User Type"].value_counts().to_frame)

    # Display counts of gender
    if city != "Washington" :
        print (df["Gender"].value_counts().to_frame)

    # Display earliest, most recent, and most common year of birth
        print ("The earliest year of birth : ",int(df["Birth Year"].min()))
        print ("The most recent year of birth : ",int(df["Birth Year"].max()))
        print ("The most common year of birth : ",int(df["Birth Year"].mode()[0]))
    else :
        print ("This data ONLY Available for Washington")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
#for 5 rows requirement 
def MoreData(df) :
    print ("Raw data is available to view")
    
    index = 0
    uInput= input("Do you like to display 5 raw data , type yes or no \n").lower()
    if uInput not in ["yes","no"]:
        print("sorry invalid answer , type yes or no ")
        uInput = input("Do you like to display 5 raw data , type yes or no \n").lower()
    elif uInput != "yes" :
        print("thank you")
    else :
        while index+5 < df.shape[0] :
            print(df.iloc[index:index+5])
            index+=5
            uInput = input("Do you like to display 5 more raw data , type yes or no \n").lower()
            if uInput != "yes" :
                print("Thank you")
                break
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        MoreData(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()