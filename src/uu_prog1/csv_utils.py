# src/uu_prog1/csv_utils.py
import csv


# CO2_EMISSIONS_DATA = "./data/CO2Emissions_filtered.csv"


def load_csv(filename):
    """
    takes a string filename as argument and returns a
    dictionary that takes the country code (all in the
    lowercases) as the key and the list of yearly CO2
    emission history as the value.
    """
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
    return {v[1].lower(): list(map(float, v[3:])) for v in reader[1:]}
