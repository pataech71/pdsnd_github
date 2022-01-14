import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please chose one of the three cities you want to filter data from. Please type either: chicago, new york or washington')
    city = city.lower()

    while (city != 'chicago') and (city != 'new york') and (city != 'washington'):
        print('please enter a correct value for city')
        city = input('Please type in either: chicago or new york or washington ')
        city = city.lower()

    # get user input for month (all, january, february, ... , june)
    month = input('Which month do you want to filter the data? January, February, March, April, May, June or "All" for all the months ')
    month = month.title()
    while (month != 'January') and (month != 'February') and (month != 'March') and (month != 'April') and (month != 'May') and (month != 'June') and (month != 'All'):
        print('Please enter a valid month.')
        month = input('Please enter: January, February, March, April, May, June or "All" for all the months ')
        month = month.title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please type in the name of the week day you want to filter data from. Please type in: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type "All" for no filter ')
    day = day.title()
    while (day != 'Monday') and (day != 'Tuesday') and (day != 'Wednesday') and (day != 'Thursday') and (day != 'Friday') and (day != 'Saturday') and (day != 'Sunday') and (day != 'All'):
        print('Please enter a valid day.')
        day = input('Please type a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Or type "all" for no filter.')
        day = day.title()


    print('-'*40)
    print(f'\nThe choosen city is {city} on the month of {month} on the day of {day}')

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
    fileinput = CITY_DATA[city]
    df = pd.read_csv(fileinput)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    if month != 'All':
        df = df[df['Start Time'].dt.month_name() == month]

    if day != 'All':
        df = df[df['Start Time'].dt.day_name() == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = int(df['Start Time'].dt.month.mode())
    print(f'The most popular month is {most_common_month} ')

    # display the most common day of week
    most_common_day = df['Start Time'].dt.day_name().mode()[0]
    print(f'The most pupular day is {most_common_day} ')

    # display the most common start hour
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print(f'The most popular start hour is {most_common_start_hour} ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = str(df['Start Station'].mode()[0])
    valuestart = df['Start Station'].value_counts()[0]
    print(f'The most used Start Station is {most_used_start_station} with {valuestart} starting trips')

    # display most commonly used end station
    most_used_end_station = str(df['End Station'].mode()[0])
    valueend = df['End Station'].value_counts()[0]
    print(f'The most used End Station is {most_used_end_station} with {valueend} ending trips')

    # display most frequent combination of start station and end station trip
    combination = (df['Start Station'] + ' '+ df['End Station'])
    most_frequent_combination = combination.mode()[0]
    print(f'The most frequent combination is {most_frequent_combination}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = ((df['Trip Duration'].sum())/60)/60
    print(f'the total travel time is {total_travel_time} hours')

    # display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print(f'the mean travel time is {mean_travel_time} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f'The break down by user type is : \n{user_type} \n')

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(f'The break down by gender is : \n{gender} \n')
    else:
        print('Not statistics available for Gender in the chosen city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        max_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()
        print(f'The oldest user was born in {min_birth_year}\nThe youngest user was born in {max_birth_year}\nThe most common year of birth of users is {most_common_birth_year[0]} ')
    else:
        print('Not statistics available for Birth Year in the chosen city \n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
