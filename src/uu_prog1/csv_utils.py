# src/uu_prog1/csv_utils.py

# import debug
import csv

# CO2_EMISSIONS_DATA = "./data/CO2Emissions_filtered.csv"


# @debug
def load_csv(filename):
    """
    takes a string filename as argument and returns a dictionary
    with the country code (lowercase) as key and the list of
    yearly CO2 emission history as value.
    """
    d = dict()
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        for index, line in enumerate(reader):
            if index != 0:
                d[line[1].lower()] = list(map(float, line[3:]))
    return d
