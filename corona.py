#!/usr/bin/env python

# Modified by : Priyanshu(@LordShenron) based on Emanuel Ramirez's script.
# This script is alot simpler and simply just show you the stats without needing any user Input.
# As for stats it shows only for India and Worldwide.
# I also removed all uneeded functions and userinput verifications.

import json
import requests

def india_stats(url):
    response = requests.get(url, headers={"User-Agent": "XY"})
    content = json.loads(response.content.decode())
    print('****** DAILY COVID-19 UPDATE ****** \n')
    print('COVID-19 STATS FOR INDIA \n')
    print('Country:', content['countrydata'][0]['info']['title'])
    print("Total Cases: {val:,}".format(val=content['countrydata'][0]['total_cases']))
    print("Total New cases: {val:,}".format(val=content['countrydata'][0]['total_new_cases_today']))    
    print('Total Active Cases: {val:,}'.format(val=content['countrydata'][0]['total_serious_cases']))
    print('Total Cases Recovered: {val:,}'.format(val=content['countrydata'][0]['total_recovered']))
    print('Total Deaths Today: {val:,}'.format(val=content['countrydata'][0]['total_new_deaths_today']))    
    print('Total Deaths Reported: {val:,}'.format(val=content['countrydata'][0]['total_deaths']))
    death_rate = ((int(content['countrydata'][0]['total_deaths'])) /\
          (int(content['countrydata'][0]['total_cases']))) * 100
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')

def world_stats(url):
    response = requests.get(url, headers={"User-Agent": "XY"})
    content = json.loads(response.content.decode())
    print('COVID-19 STATS WORLDWIDE \n')
    print("Total cases: {val:,}".format(val=content['results'][0]['total_cases']))
    print("Total New cases: {val:,}".format(val=content['results'][0]['total_new_cases_today']))
    print("Total Recovered cases: {val:,}".format(val=content['results'][0]['total_recovered']))
    print("Total Unresolved cases: {val:,}".format(val=content['results'][0]['total_unresolved']))
    print("Total Deaths: {val:,}".format(val=content['results'][0]['total_deaths']))
    print("Total Active Cases: {val:,}".format(val=content['results'][0]['total_active_cases']))
    print("Total Serious Cases: {val:,}".format(val=content['results'][0]['total_serious_cases']))
    death_rate = ((int(content['results'][0]['total_deaths'])) /\
          (int(content['results'][0]['total_cases']))) * 100
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')


if __name__ == "__main__":
    INDIA_URL = 'https://thevirustracker.com/free-api?countryTotal=IN'
    india_stats(INDIA_URL)
    WORLD_URL = 'https://thevirustracker.com/free-api?global=stats'
    world_stats(WORLD_URL)