#!/usr/bin/env python3

# Modify this script to get and store
# tithi of different years and months

from tithi.scraper import Scraper
import json


OUT_FILE = "data.json"
INIT_YEAR = 2070
END_YEAR = 2072


if __name__ == "__main__":

    # Get tithi of each year and month

    tithis = []

    year = INIT_YEAR
    while year <= END_YEAR:

        for month in range(12):
            print("%04d-%02d" % (year, month+1))

            s = Scraper(2072, month+1)
            tithis += s.get_tithis()

        year += 1

    # Write to json file
    with open(OUT_FILE, 'w') as file:
        json.dump(tithis, file)
