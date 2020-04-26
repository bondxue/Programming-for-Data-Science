import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        if city.lower() in CITY_DATA.keys():
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Would you like to filter the data by month (January, February, March, April, May, or June)? '
        'Type "all" for no month filter.\n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day would like to filter (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)? '
        'Type "all" for no day filter.\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.capitalize()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.capitalize()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month of travel: {}'.format(df['month'].value_counts().idxmax()))


    # TO DO: display the most common day of week
    print('Most common day of travel: {}'.format(df['day_of_week'].value_counts().idxmax()))


    # TO DO: display the most common start hour
    print('Most common start hour: {}'.
    format(datetime.datetime.strptime(str(df['Start Time'].dt.hour.value_counts().idxmax()), "%H").strftime("%I %p")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: {}'.format(df['Start Station'].value_counts().idxmax()))

    # TO DO: display most commonly used end station
    print('Most commonly used end station: {}'.format(df['End Station'].value_counts().idxmax()))

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip:\n{}'
    .format(df.groupby(['Start Station', 'End Station']).size().nlargest(1).to_string()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: {}'.format(datetime.timedelta(seconds=int(df['Trip Duration'].sum()))))

    # TO DO: display mean travel time
    print('Mean travel time: {}'.format(datetime.timedelta(seconds=int(df['Trip Duration'].mean()))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n{}'.format(df['User Type'].value_counts().to_string()))

    # TO DO: Display counts of gender
    print('Counts of gender:')
    try:
        print(df['Gender'].value_counts().to_string())
    except:
        print('Washington does not include gender information.')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nEarliest, Latest & Most Common Date of Birth:')
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].value_counts().idxmax()))
    except:
        print('Washington does not include date of birth information')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    """Iterate and show 5 entries of raw data at a time."""

    show_more = True
    index = 0
    response = input('Do you want to see 5 lines data entries? Yes or No?\n')
    while show_more:

        if response.lower() == 'yes':
            print(df.loc[index:index+4, :])
            index += 5
            response = input('Want see 5 more? Yes or No?\n')
        if response.lower() == 'no':
            show_more = False
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
