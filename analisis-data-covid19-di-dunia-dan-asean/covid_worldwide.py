# Import libraries
import json
import numpy as np
import pandas as pd
import requests
import datetime
from datetime import date
import matplotlib.pyplot as plt

# Function to load API
def get_json(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

# Call Covid19 API for today's worldwide status
covid_url = 'https://covid19-api.org/api/status?date=' + date.today().strftime('%Y-%m-%d')
df_covid_worldwide = pd.json_normalize(get_json(covid_url))

# Get countries data
countries_url = 'https://covid19-api.org/api/countries'
df_countries = pd.json_normalize(get_json(countries_url))
df_countries = df_countries.rename(columns={'alpha2':'country'})[['name','country']]

# Merge Covid19 and countries data
df_covid_worldwide = pd.merge(df_countries, df_covid_worldwide, on='country')

# Change String datetime to Python datetime object
df_covid_worldwide['last_update'] = pd.to_datetime(df_covid_worldwide['last_update'], format='%Y-%m-%d %H:%M:%S')

# Change the value of 'last_update' column. So that, it displays only the date
df_covid_worldwide['last_update'] = df_covid_worldwide['last_update'].apply(lambda x: x.date())

# Calculate fatality ratio in percent
df_covid_worldwide['fatality_ratio'] = (df_covid_worldwide['deaths'] / df_covid_worldwide['cases']) * 100

# Show top 20 countries which have the highest fatality ratio
df_top_20_fatality_rate = df_covid_worldwide.sort_values(by='fatality_ratio', ascending=False).head(20)

# Visualize the top 20 countries which have the highest fatality ratio
plt.figure(figsize=(10,6))
x = df_top_20_fatality_rate['name']
y = df_top_20_fatality_rate['fatality_ratio']
bars = plt.bar(x,y)
plt.xlabel('Country Name')
plt.ylabel('Fatality Rate')
plt.title('Top 20 Highest Fatality Rate Countries Worldwide')
plt.xticks(rotation=90, fontsize='8')
plt.yticks(fontsize='8')
plt.tight_layout()
for i, number in enumerate(y):
    plt.text(x=i-0.35, y=number+0.004, s=str(round(number, 2))+'%', weight='normal', fontsize='6')
plt.show()

# Shows the top 20 countries by case
df_top_20_by_cases = df_covid_worldwide.sort_values(by='cases', ascending=False).head(20)

# Visualize the top 20 countries which have the most case
plt.figure(figsize=(10,6.5))
x = df_top_20_by_cases['name']
y = df_top_20_by_cases['cases']
bars = plt.bar(x,y)
plt.xlabel('Country Name')
plt.ylabel('Number of Cases')
plt.title('Top 20 Highest Number of Case Worldwide')
plt.xticks(rotation=90, fontsize='8')
plt.yticks(fontsize='8')
plt.tight_layout()
for i, number in enumerate(y):
    plt.text(x=i-0.35, y=number+0.004, s=number, weight='normal', fontsize='6')
plt.show()