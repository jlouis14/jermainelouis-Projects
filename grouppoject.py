import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Specify the file path to the CSV file
file_path = ("/Users/abdulmujeebahmed/Desktop/LA_County_COVID_Cases.csv")


# Read the CSV file using Pandas
df = pd.read_csv(file_path)


# Shortening the data frame by removing excess rows
df.drop(df.index[301:], inplace=True)


df.drop('people_tested', axis=1, inplace=True)
df.drop('Lat', axis=1, inplace=True)
df.drop('Lon', axis=1, inplace=True)
df.drop('fips', axis=1, inplace=True)
df.drop('state', axis=1, inplace=True)


df['date'] = pd.to_datetime(df['date'])


df = df.sort_values(by='date')


df.to_csv('sorted_file.csv', index=False)


# Print the DataFrame
print(df, '\n')


# Set display options to show all columns and rows
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


mean_county_cases = df['cases'].mean()
mean_county_deaths = df['deaths'].mean()
median_county_cases = df['cases'].median()
median_county_deaths = df['deaths'].median()
var_county_cases = df['cases'].var()
var_county_deaths = df['deaths'].var()
std_dev_county_cases = df['cases'].std()
std_dev_county_deaths = df['deaths'].std()


print('Mean For Number of County Cases:', mean_county_cases, '\n')
print('Mean For Number of County Deaths:', mean_county_deaths, '\n')
print('Median For Number of County Cases:', median_county_cases, '\n')
print('Median For Number of County Deaths:', median_county_deaths, '\n')
print('Variance For Number of County Cases:', var_county_cases, '\n')
print('Variance For Number of County Deaths:', var_county_deaths, '\n')
print('Standard Deviation For Number of County Cases:', std_dev_county_cases, '\n')
print('Standard Deviation For Number of County Deaths:', std_dev_county_deaths, '\n')


mean_state_cases = df['state_cases'].mean()
mean_state_deaths = df['state_deaths'].mean()
median_state_cases = df['state_cases'].median()
median_state_deaths = df['state_deaths'].median()
var_state_cases = df['state_cases'].var()
var_state_deaths = df['state_deaths'].var()
std_dev_state_cases = df['state_cases'].std()
std_dev_state_deaths = df['state_deaths'].std()


print('Mean For Number of State Cases:', mean_state_cases, '\n')
print('Mean For Number of State Deaths:', mean_state_deaths, '\n')
print('Median For Number of State Cases:', median_state_cases, '\n')
print('Median For Number of State Deaths:', median_state_deaths, '\n')
print('Variance For Number of State Cases:', var_state_cases, '\n')
print('Variance For Number of State Deaths:', var_state_deaths, '\n')
print('Standard Deviation For Number of State Cases:', std_dev_state_cases, '\n')
print('Standard Deviation For Number of State Deaths:', std_dev_state_deaths, '\n')


fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
ax.plot(df['date'], df['cases'], label='LA Cases')
ax.plot(df['date'], df['state_cases'], label='State Cases')


from matplotlib.dates import DateFormatter
date_form = DateFormatter("%Y-%m-%d")
ax.xaxis.set_major_formatter(date_form)


ax.set(title='Running Number of Cases (State vs LA)', xlabel='Date', ylabel='Number of Cases')
ax.legend(['Number of Cases'])
plt.legend()
plt.show()


new_county_cases_total = df['new_cases'].sum()
new_county_death_total = df['new_deaths'].sum()
fig, ax = plt.subplots()
values = [new_county_cases_total, new_county_death_total]
labels = ['New Cases in LA', 'New Deaths in LA']
ax.pie(values, labels=labels, autopct='%1.1f%%')
ax.set_title('New Cases vs New Deaths in LA')
plt.show()


fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)
grouped_df = df.groupby('date')['new_cases', 'new_deaths'].sum()
ax.bar(grouped_df.index, grouped_df['new_cases'], label='New Cases in LA')
ax.bar(grouped_df.index, grouped_df['new_deaths'], label='New Deaths in LA')
ax.set(title='Number of New Cases vs New Deaths in LA Over Time', xlabel='Date', ylabel='Number of (Cases or Deaths)')
plt.legend()
plt.show()


fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111)
x = df['date']
y1 = df['new_deaths']
y2 = df['new_state_deaths']
plt.scatter(x, y1, label='New LA Deaths')
plt.scatter(x, y2, label='New State Deaths')
plt.legend()
plt.title('Scatter Plot of New Deaths in LA VS New Deaths in California over Time')
plt.xlabel('Date')
plt.ylabel('Number of New Deaths')
plt.show()
