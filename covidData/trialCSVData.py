import csv
from collections import Counter 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import geonamescache

# from matplotlib.patches import Polygon
# from matplotlib.collections import PatchCollection
# from mpl_toolkits.basemap import Basemap
treatments = [
    ["Plasma", 0],
    ["Vaccine", 0],
    ["Alternative therapy", 0],
    ["Dexamethasone", 0],
    ["Acalabrutinib", 0],
    ["Sarilumab", 0],
    ["JAKi", 0],
    ["Corticosteroids", 0],
    ["Remdesivir", 0],
    ["Vitamins", 0],
    ["Ivermectin", 0],
    ["Antivirals", 0]
]

def getTreatmentTypes():
    with open('/Users/alexpreston/Work/Coding/GPQuants/covidData/trials.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                
                for treatment in treatments:
                    if(row[14].find(treatment[0]) > -1):
                        treatment[1] = treatment[1] + 1
    
    treatments.sort(key=lambda t: t[1], reverse=True)
    return treatments


def getTrialsByCountry():
    countries = []
    with open('/Users/alexpreston/Work/Coding/GPQuants/covidData/trials.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            countries.append(row[3])
        countryTrialFrequencies = list(Counter(countries).most_common(10))

    return countryTrialFrequencies

print(getTrialsByCountry())
print(getTreatmentTypes())


def loadMap():
    num_colors = 9
    filename = "/Users/alexpreston/Work/Coding/GPQuants/covidData/trials.csv"
    year = '2012'
    cols = ['Country Name', 'Country Code', year]
    title = 'Forest area as percentage of land area in {}'.format(year)
    imgfile = 'img/test.png'

    gc = GeonamesCache()
    iso3_codes = list(gc.get_dataset_by_key(gc.get_countries(), 'iso3').keys())
    df = pd.read_csv(filename, skiprows=1, usecols=cols)
    df.set_index('Country Code', inplace=True)
    df = df.ix[iso3_codes].dropna() # Filter out non-countries and missing values.

from geonamescache.mappers import country
mapper = country(from_key='name', to_key='iso3')

iso3 = mapper('Spain') # iso3 is assigned ESP
print(iso3)