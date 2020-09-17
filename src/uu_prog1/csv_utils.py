# src/uu_prog1/csv_utils.py

import csv


def load_csv(filename):
    """
    Takes a string filename as argument and returns a dictionary
    with the country code (lowercase) as key and the list of
    yearly CO2 emission history as value.
    File is CO2Emissions_filtered.csv. First row is header.
    Fields are country_name, country_code, indicator_name and
    then years from 1960 to 2014. Data from col 3 with first col 0.
    """
    d = dict()
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for index, line in enumerate(reader):
            if index != 0:
                d[line[1].lower()] = list(map(float, line[3:]))
    return d
