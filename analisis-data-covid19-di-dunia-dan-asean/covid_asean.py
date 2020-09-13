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

# List of countries in ASEAN
asean_countries = ['ID','TH','SG','MY','PH','VN','BN','MM','KH']

# Visualize ASEAN countries by case
plt.figure(figsize=(8,6))
for country in asean_countries:
    country_data = df_covid_worldwide['country'] == country

    x = df_covid_worldwide[country_data]['name']
    y = df_covid_worldwide[country_data]['cases']
    plt.bar(x,y)
    plt.xlabel('Country Name')
    plt.ylabel('Number of Cases')
    plt.title('Fatality Rate of Countries in ASEAN')
    plt.xticks(rotation=45, fontsize='8')
    plt.yticks(fontsize='8')
    plt.tight_layout()
    for i, number in enumerate(y):
        plt.text(x, y, s=number, weight='normal', fontsize='6')
plt.show()

# Visualize ASEAN countries by fatality ratio
plt.figure(figsize=(8,6))
for country in asean_countries:
    country_data = df_covid_worldwide['country'] == country

    x = df_covid_worldwide[country_data]['name']
    y = df_covid_worldwide[country_data]['fatality_ratio']
    plt.bar(x,y)
    plt.xlabel('Country Name')
    plt.ylabel('Fatality Rate')
    plt.title('Covid Status in ASEAN')
    plt.xticks(rotation=45, fontsize='8')
    plt.yticks(fontsize='8')
    plt.tight_layout()
    for i, number in enumerate(y):
        plt.text(x, y, s=str(round(number, 2))+'%', weight='normal', fontsize='6')
plt.show()

# Get ASEAN case timeline
i = 0
for country in asean_countries:
    covid_timeline_url = 'https://covid19-api.org/api/timeline/' + country
    df_covid_timeline = pd.json_normalize(get_json(covid_timeline_url))
    df_covid_timeline['last_update'] = pd.to_datetime(df_covid_timeline['last_update'], format='%Y-%m-%d %H:%M:%S')
    df_covid_timeline['last_update'] = df_covid_timeline['last_update'].apply(lambda x: x.date())

    if i == 0:
        df_covid_timeline_merged = df_covid_timeline
    else:
        df_covid_timeline_merged = df_covid_timeline.append(df_covid_timeline_merged, ignore_index = True)
    i = i + 1

# Merge ASEAN timeline data with country data
df_covid_asean_timeline = pd.merge(df_covid_timeline_merged, df_countries, on='country')

# Get Covid19 timeline in ASEAN from 11 March 2020
df_covid_asean_timeline = df_covid_asean_timeline[(df_covid_asean_timeline['last_update'] >= datetime.date(2020, 3, 11))]

# Visualize Covid19 timeline in ASEAN
# plt.clf()
for country in asean_countries:
    country_data = df_covid_asean_timeline['country'] == country
    x = df_covid_asean_timeline[country_data]['last_update']
    y = df_covid_asean_timeline[country_data]['cases']
    plt.plot(x, y, label = country)

plt.legend()
plt.xlabel('Record Date')
plt.ylabel('Total Cases')
plt.title('Asean Covid19 Cases Comparison')
plt.tight_layout()
plt.show()