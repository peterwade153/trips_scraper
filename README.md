# trips_scraper

This is a complete scrapy spider which pulls trips data .i.e name, prices, activities, tour types, departures dates, duration days and country.
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
