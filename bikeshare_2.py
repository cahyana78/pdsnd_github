import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    # eduacational source for while: https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response

    while True:
        city = str(input('Please choose one of the cities (Chicago, New York City, Washington)')).lower()

        if city not in ("chicago", "new york city", "washington"):
            print('Please choose the correct city')

        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Please choose the month (January, February, March, April, May, or June or all)')).lower()
        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print('Please choose the correct month')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose the day or all').lower()
        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
            print('Please choose the correct day')
            continue
        else:
            break

    print('-' * 40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')


start_time = time.time()
# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# TO DO: display the most common month
## extract month from the Start Time column to create an month column
df['month'] = df['Start Time'].dt.month
## find the most popular month
popular_month = df['month'].mode()[0]

# TO DO: display the most common day of week
## extract month from the Start Time column to create an month column
df['week'] = df['Start Time'].dt.week
## find the most popular month
popular_week = df['week'].mode()[0]

# TO DO: display the most common start hour
## extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

## find the most popular hour
popular_hour = df['hour'].mode()[0]

print('Most Popular Month:', popular_month)
print('Most Popular Week:', popular_week)
print('Most Popular Start Hour:', popular_hour)

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)

print("\nThis took %s seconds." % (time.time() - start_time))
print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    ## print value counts for each user type
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    ## print value counts for each gender

    while True:
        if ("Gender" in df.columns):
            gender = df['Gender'].value_counts()
            print('gender')
            print(gender)
            break
        else:
            print('Washington does not have data about gender of customer')
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        # to find a columns in df
        if ("Birth Year" in df.columns):
            earliest = min(df['Birth Year'])
            recent = max(df['Birth Year'])
            common_year = df['Birth Year'].mode()[0]
            print('Earliest birth year is in: %d' % earliest)
            print('Most recent birth year is in: %d' % recent)
            print('Most common birth year is in: %d' % common_year)
            break
        else:
            print('Washington does not have data about birth year of customer')
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
