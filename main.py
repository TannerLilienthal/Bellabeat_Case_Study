import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

daily_activity = pd.read_csv("fitbit_data/daily_activity.csv")
# headers = (id, activity_date, total_steps, total_distance, tracker_distance,
#           logged_activites_distance, very_active_distance, moderately_active_distance,
#           light_activity_distance, sedentary_active_distance, very_active_minutes,
#           fairly_active_minutes, lightly_active_minutes, sedentary_minutes,
#           calories, day_of_week)
day_sleep = pd.read_csv("fitbit_data/day_sleep.csv")
# headers = (id, sleep_date, total_sleep_records, total_sleep_minutes,
#           total_time_in_bed, day_of_week)
heartrate_seconds = pd.read_csv("fitbit_data/heartrate_seconds.csv")
# headers = (id, time, heartrate, day_of_week)
hourly_ativity = pd.read_csv("fitbit_data/hourly_activity.csv")
# headers = (id, activity_hour, calories, total_intensity, average_intensity,
#           step_total, day_of_week)
minute_calories = pd.read_csv("fitbit_data/minute_calories.csv")
# headers = (id, activity_minute, calories, day_of_week)
minute_intensities = pd.read_csv("fitbit_data/minute_intensities.csv")
# headers = (id, activity_minute, intensity, day_of_week)
minute_steps = pd.read_csv("fitbit_data/minute_steps.csv")
# headers = (id, activity_minute, steps, day_of_week)
weight_log = pd.read_csv("fitbit_data/weight_log.csv")
# headers = (id, date, weight_kg, weight_lb, bmi, is_manual_report, day_of_week)


