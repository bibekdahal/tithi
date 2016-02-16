import requests
import bs4


BASE_URL = "http://www.nepalicalendar.com/index.php"


# Scraper class to grab tithi data from web
class Scraper:

    def __init__(self, year, month):
        self.year = year
        self.month = month

        self.url = BASE_URL + \
            "?ny=%d&nm=%02d" % (self.year, self.month)

        # Get the html from web page and parse using BeautifulSoup
        self.response = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.response.text, "lxml")

    def get_tithis(self):

        self.tithis = []

        # Get tithi for each date in the month
        for i in range(32):
            date = (self.year, self.month, i+1)
            date_str = "%04d-%02d-%02d" % date

            # Get a "div" tag for the day
            day = self.soup.find('div', {"ids": date_str})

            # If day exists, get the tithi
            if day:
                tithi = day.find('div', {"id": "tithi"}).text.strip()
                if tithi:
                    self.tithis.append(
                        {"date": date_str, "tithi": tithi}
                    )

        return self.tithis
