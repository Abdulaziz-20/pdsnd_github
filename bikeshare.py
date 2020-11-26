import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

monthList = ['january', 'february', 'march', 'april', 'may', 'june']

dayList = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cityName = input('Please Enter the city name: ').lower()
    while(True):
        if((cityName == 'chicago') or (cityName == 'new york city') or (cityName == 'washington')):
            break
        cityName = input('Please Enter a correct city name: ').lower()

    
    choice = input('do you prefer to search by month or day or none: ').lower()

    while True:
        if (choice == 'month') or (choice == 'day') or (choice == 'none'):
            break
        choice = input('please enter a month or day or none if do not want to search by date: ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'no month selected'
    if choice == 'month': 
        month = input('please enter the month you want to search for: ').lower()
        while True:
            if month in monthList or month == 'all':
                break
            month = input('please enter a correct month: ').lower()
                
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'no day selected'
    if choice == 'day':
        day = input('please enter the day you want to search by: ').lower()
        while True:
            if day in dayList or day == 'all':
                break
            day = input('please enter a correct day: ').lower()
            
    print('-'*40)
    return cityName, month, day


def load_data(cityName, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    dataFrame = pd.read_csv(CITY_DATA[cityName])
    dataFrame['Start Time'] = pd.to_datetime(dataFrame['Start Time'])
    dataFrame['hour'] = dataFrame['Start Time'].dt.hour
    dataFrame['month'] = dataFrame['Start Time'].dt.month_name()
    dataFrame['day'] = dataFrame['Start Time'].dt.weekday_name
    
    if (month in monthList) and (day == 'no day selected'):
        return (dataFrame[dataFrame['month']==month.title()])
    elif (month == 'no month selected') and (day in dayList):
        return (dataFrame[dataFrame['day'] == day.title()])

    return dataFrame


def time_stats(dataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonMonth = dataFrame['month'].mode()[0]
    print(' The most common month in the data frame is: ', commonMonth)
    # TO DO: display the most common day of week
    commonDay = dataFrame['day'].mode()[0]
    print(' The most common day in the data frame is: ', commonDay)


    # TO DO: display the most common start hour
    commonStartHour = dataFrame['hour'].mode()[0]
    print(' The most common start hour in the data frame is: ', commonStartHour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(dataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonStartStation = dataFrame['Start Station'].mode()[0]
    print('The most commonly used start station is: ', commonStartStation)
    # TO DO: display most commonly used end station
    commonEndStation = dataFrame['Start Station'].mode()[0]
    print('The most commonly used end station is: ', commonEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    dataFrame['fullTrip'] = dataFrame['Start Station'] + ' ' + dataFrame['End Station']
    fullTrip = dataFrame['fullTrip'].mode()[0]
    print('The most frequent combination of start station and end station trip is:', fullTrip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(dataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is: ', dataFrame['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time is: ', dataFrame['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(dataFrame, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
#     if ((dataFrame['']==) or ())
    print('the count of users type is: ', dataFrame['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    if city != 'washington':
        print('the number of gender types is: ', dataFrame['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('\nthe earliest year of birth is: ', dataFrame['Birth Year'].min())
        print('\nthe most recent year of birth is: ', dataFrame['Birth Year'].max())
        print('\nthe most common year of birth is: ', dataFrame['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def printingDataFrame(dataFrame):
    # This function is used to print 5 users info by one printing order, it prints 5 each time until the user enters 'no' after that it will print the number of printed users 'index'.
    index = 0
    while True:
        
        print('\n',dataFrame.iloc[index])
        index +=1
<<<<<<< HEAD
            # The %5 is for printing 5 elements only.
=======
        # The %5 is for printing 5 elements from the dataFrame
>>>>>>> documentation
        if(index % 5 ==0):
            if 'yes' == input('\nWould you like to print the data? Enter yes or no.\n').lower():
                continue
            else:
            #this prints the total printed users
                print('The number of printed users= ', index)
                break
                
def main():
# This is the main function where it will run the whole code
    while True:
        city, month, day = get_filters()
        dataFrame = load_data(city, month, day)
        time_stats(dataFrame)
        station_stats(dataFrame)
        trip_duration_stats(dataFrame)
        user_stats(dataFrame, city)
        if  input('\nWould you like to print the data? Enter yes or no.\n').lower() != 'no':
            printingDataFrame(dataFrame)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
