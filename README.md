# trips_scraper

This is a complete scrapy spider built using [Scrapy](https://docs.scrapy.org/en/latest/index.html), a web crawling and scraping framework, and Python 3.6 

The spider pulls tourism trips data from https://www.bookmundi.com specifically for the East-african region i.e Uganda, Kenya and Tanzania.

The data includes name(short description), prices, activities, tour types, departures dates, duration days and country.

The Scraped data is stored in a temporary directory `tmp` as a `trips.csv` file.

### Installation

Create a virtual env and activate it.

Clone the project
<pre>
git clone https://github.com/peterwade153/trips_scraper.git
</pre>

Install Dependencies.

<pre>
pip install requirements.txt
</pre>

### To run the spider.
Use the command below
<pre>
scrapy crawl trips
</pre>
