import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', 40)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:20,.2f}'.format

daily_activity = pd.DataFrame(pd.read_csv("fitbit_data/daily_activity.csv"))
daily_activity.name = 'daily_activity'
# headers = (id, activity_date, total_steps, total_distance, tracker_distance,
#           logged_activites_distance, very_active_distance, moderately_active_distance,
#           light_activity_distance, sedentary_active_distance, very_active_minutes,
#           fairly_active_minutes, lightly_active_minutes, sedentary_minutes,
#           calories, day_of_week)
day_sleep = pd.DataFrame(pd.read_csv("fitbit_data/day_sleep.csv"))
day_sleep.name = 'day_sleep'
# headers = (id, sleep_date, total_sleep_records, total_sleep_minutes,
#           total_time_in_bed, day_of_week)
heartrate_seconds = pd.DataFrame(pd.read_csv("fitbit_data/heartrate_seconds.csv"))
heartrate_seconds.name = 'heartrate_seconds'
# headers = (id, time, heartrate, day_of_week)
hourly_activity = pd.DataFrame(pd.read_csv("fitbit_data/hourly_activity.csv"))
hourly_activity.name = 'hourly_activity'
# headers = (id, activity_hour, calories, total_intensity, average_intensity,
#           step_total, day_of_week)
minute_calories = pd.DataFrame(pd.read_csv("fitbit_data/minute_calories.csv"))
minute_calories.name = 'minute_calories'
# headers = (id, activity_minute, calories, day_of_week)
minute_intensities = pd.DataFrame(pd.read_csv("fitbit_data/minute_intensities.csv"))
minute_intensities.name = 'minute_intensities'
# headers = (id, activity_minute, intensity, day_of_week)
minute_steps = pd.DataFrame(pd.read_csv("fitbit_data/minute_steps.csv"))
minute_steps.name = 'minute_steps'
# headers = (id, activity_minute, steps, day_of_week)
weight_log = pd.DataFrame(pd.read_csv("fitbit_data/weight_log.csv"))
weight_log.name = 'weight_log'
# headers = (id, date, weight_kg, weight_lb, bmi, is_manual_report, day_of_week)

tables = [daily_activity, day_sleep, heartrate_seconds, hourly_activity,
          minute_calories, minute_intensities, minute_steps, weight_log]


def print_out_summary_statistics():
    for table in tables:
        numeric_data_types = ['int64', 'float64']
        numeric_columns = []
        for column in table:
            if table[column].dtype in numeric_data_types:
                numeric_columns.append(column)
        print(f'==========={table.name}===========')
        print(table.describe())


# check amount of hours spent sedentary, talk about this
def sedentary_hours_visual():
    # sectors for 0-8hr, 8-12, 12-16, 16-20, 20-24, and 24
    zero_to_eight = daily_activity[daily_activity['sedentary_minutes'] < 480]
    eight_to_twelve = daily_activity[(daily_activity['sedentary_minutes'] >= 480) &
                                     (daily_activity['sedentary_minutes'] < 720)]
    twelve_to_sixteen = daily_activity[(daily_activity['sedentary_minutes'] >= 720) &
                                     (daily_activity['sedentary_minutes'] < 960)]
    sixteen_to_twenty = daily_activity[(daily_activity['sedentary_minutes'] >= 960) &
                                     (daily_activity['sedentary_minutes'] < 1200)]
    twenty_to_twentyfour = daily_activity[(daily_activity['sedentary_minutes'] >= 1200) &
                                     (daily_activity['sedentary_minutes'] < 1440)]
    twentyfour = daily_activity[daily_activity['sedentary_minutes'] == 1440]

    # make pie showing consecutive hours sedentary
    labels = ['0 to 8 hrs', '8 to 12 hrs', '12 to 16 hrs', '16 to 20 hrs', '20 to 24 hrs', '24 hrs']
    sizes = [zero_to_eight['id'].count(), eight_to_twelve['id'].count(), twelve_to_sixteen['id'].count(),
             sixteen_to_twenty['id'].count(), twenty_to_twentyfour['id'].count(), twentyfour['id'].count()]
    fig1, pie_chart = plt.subplots()
    pie_chart.pie(sizes, labels=labels, explode=(0, 0, 0, 0, 0, 0.1), autopct='%1.1f%%', startangle=90)
    plt.title('Frequency of Sedentary Hours')
    pie_chart.axis('equal')
    plt.show()


# check number of logged events per id
def logged_events_visual():
    # gather time of day rows
    plt.hist(daily_activity['day_of_week'], bins=7, width=0.5, edgecolor='black', color='red')
    plt.title('Frequency of Daily Logs')
    plt.xlabel('Day of Week')
    plt.ylabel('Frequency')
    plt.show()


# check what type of activity is the most frequent, to aid who to market to
def type_of_activity_visual():
    # make a line graph that has separate lines for each type of activity
    sorted_dates = daily_activity['activity_date'].sort_values()
    plt.plot(sorted_dates, daily_activity['very_active_minutes'].cumsum(), color='blue')
    plt.plot(sorted_dates, daily_activity['fairly_active_minutes'].cumsum(), color='red')
    plt.plot(sorted_dates, daily_activity['lightly_active_minutes'].cumsum(), color='green')
    plt.title('Cumulative User Minutes Over Time (30 days)')
    plt.xticks([0, 15, 30], ['Day 1', 'Day 15', 'Day 30'])
    plt.xlabel('Time')
    plt.ylabel('Total Minutes')
    plt.show()


# OTHER POTENTIAL RELATIONSHIPS TO CHECK FOR
# -check average length of intensity, shorter or longer and is there a correlation between length & intensity
# -check total_time_in_bed vs different activity types

# print_out_summary_statistics()
# sedentary_hours_visual()
# logged_events_visual()
type_of_activity_visual()
