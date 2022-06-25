import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime as dt

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
hourly_ativity = pd.DataFrame(pd.read_csv("fitbit_data/hourly_activity.csv"))
hourly_ativity.name = 'hourly_activity'
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

tables = [daily_activity, day_sleep, heartrate_seconds, hourly_ativity,
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


def compare_steps_to_calories():
    plt.scatter(daily_activity.total_steps, daily_activity.calories, c=daily_activity.calories, cmap=mpl.cm.coolwarm)
    plt.colorbar(orientation='vertical')
    plt.show()


print_out_summary_statistics()
compare_steps_to_calories()

