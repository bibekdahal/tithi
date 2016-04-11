import requests
import bs4


BASE_URL = "http://www.ashesh.com.np/nepali-calendar/"

MONTHS = ["Baishakh", "Jestha", "Ashadh", "Shrawan",
          "Bhadra", "Ashwin", "Kartik", "Mangsir", "Poush",
          "Magh", "Falgun", "Chaitra"]

EN_TITHIS = ["Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi",
             "Aaunsi",
             "Purnima", "Pratipada", "Dwitiya", "Tritiya", "Chaturthi",
             "Panchami", "Sasthi", "Saptami", "Astami", "Nawami",
             "Dashami" ]


NP_TITHIS = ["एकादशी", "द्वादशी","त्रयोदशी", "चतुर्दशी",
             "औंसी",
             "पूर्णिमा", "प्रतिपदा", "द्वितीया", "तृतिया", "चतुर्थी",
             "पञ्चमी", "षष्ठी", "सप्तमी", "अष्टमी", "नवमी",
             "दशमी"]


# Scraper class to grab tithi data from web
class Scraper:

    def __init__(self, year, month):
        self.year = year
        self.month = month

        self.url = BASE_URL + \
            "?year=%d&month=%s" % (self.year, MONTHS[self.month-1])

        # Get the html from web page and parse using BeautifulSoup
        self.response = requests.get(self.url)
        self.soup = bs4.BeautifulSoup(self.response.text, "lxml")

    def get_tithis(self):

        self.tithis = []
        raw_days = self.soup.findAll('div', {"class": "date_np"})
        days = {}

        for day in raw_days:
            tithi = day.parent.find('div', {"class": "tithi"}).text.strip()
            if tithi in EN_TITHIS:
                tithi = NP_TITHIS[EN_TITHIS.index(tithi)]
            days[int(day.get_text())] = [day.get('title').strip(), tithi]

        self.tithis = []
        for i in range(32):
            if (i+1) in days:
                day = days[i+1]

                date = (self.year, self.month, i+1)
                date_str = "%04d-%02d-%02d" % date

                self.tithis.append(
                    {"date": date_str, "tithi": day[1], "extra": day[0] }
                )
                
        return self.tithis
