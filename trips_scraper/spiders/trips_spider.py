import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from trips_scraper.items import TripItem


class TripSpider(scrapy.Spider):
    name = "trips"

    def start_requests(self):
        urls = [
            "https://www.bookmundi.com/uganda",
            "https://www.bookmundi.com/kenya",
            "https://www.bookmundi.com/tanzania",
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    @staticmethod
    def _parse_country_from_url(response):
        country = response.url.split("/")[-1]
        if "?" in country:
            return country.split("?")[0]
        return country

    def parse(self, response):
        for trip in response.css("div.trips-holder > div.trips-block"):
            trip_loader = ItemLoader(item=TripItem(), selector=trip)

            trip_loader.default_output_processor = TakeFirst()
            trip_loader.add_css("name", "h4 > a.target-link::text")
            trip_loader.add_css("price", ".price-holder > span > .p::text")
            trip_loader.add_css(
                "activities", "ul.trip-info-list > li > span.txt.elps > a::text"
            )
            trip_loader.add_css("tour_type", "ul.trip-info-list > li > span.txt::text")
            trip_loader.add_css(
                "next_departure_date", "ul.departure-table > li > span::text"
            )
            trip_loader.add_css(
                "days", "span.price-holder > span > span::text", re="(\d+)"
            )

            country = TripSpider._parse_country_from_url(response)

            trip_loader.add_value("country", country)

            yield trip_loader.load_item()

        # Handle pagination, fetch next page contents
        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
