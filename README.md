tithi
-------

**tithi** is a web scraping python api for getting nepali tithi data from web pages. It obtains and stores tithi in unicode Devanagari strings.

Currently, [http://www.ashesh.com.np/nepali-calendar/](http://www.ashesh.com.np/nepali-calendar/) is used to get the tithi data.

## Dependencies

The *tithi* api is developed for python3 and depends on following python3 pacakges:

* `requests`
* `beautifulsoup4`

These may be installed with *pip*:

```
pip3 install requests beautifulsoup4
```

## Usage

The `tithi` package consists of one `scraper` module which contains the `Scraper` class that loads html for provided year and month.

```python
from tithi.scraper import Scraper


year = 2072
month = 11
s = Scraper(year, month)
```

The complete tithi data can be obtained by calling the `get_tithis()` method.

```python
tithis = s.get_tithis()
```

The tithi data are stored in a list of dictionaries, each containing a `date` and a `tithi` fields. Example of an item in the list is:

```python
{ "date" : "2072-11-01", "tithi": "पञ्चमी", "extra": "सरस्वती पुजा, वसन्तश्रावण, श्रीपञ्चमी" }
```


## The Database

Date and tithi data for several years are automatically generated and stored in a json file, which can be viewed and used by anyone. The json file is currently avaiable at [https://raw.githubusercontent.com/bibekdahal/tithi/master/data.json](https://raw.githubusercontent.com/bibekdahal/tithi/master/data.json).

The format of the json database is as follows.

```
{
	"init_year" : initial_year_in_this_database,
    "end_year" : final_year_in_this_database,
    "data" : [
    	{ "date" : "YYYY-MM-DD", "tithi": tithi_for_this_day, "extra", holiday_and_extra },
        ...
    ]
}
```
