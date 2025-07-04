from scrapy_selenium import SeleniumRequest
import scrapy


class ControllerSpider(scrapy.Spider):
    name = "controller"
    allowed_domains = ["amazon.com"]
    start_urls = [
        "https://www.amazon.com/s?k=solar+charge+controller&crid=30ACFM7F905FB&sprefix=sollar%2Caps%2C608&ref=nb_sb_ss_p13n-pd-dpltr-ranker_5_6"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5
            )

    def parse(self, response):
        products = response.xpath('//div[@data-component-type="s-search-result"]')

        for product in products:
            title = product.xpath('.//h2/span/text()').get(default='').strip()

            relative_link = product.xpath('.//h2/parent::a/@href').get()
            product_link = response.urljoin(relative_link) if relative_link else None

            price_whole = product.xpath('.//span[@class="a-price-whole"]/text()').get()
            price_fraction = product.xpath('.//span[@class="a-price-fraction"]/text()').get()
            price = f"${price_whole.strip()}.{price_fraction.strip()}" if price_whole and price_fraction else None

            list_price = product.xpath('.//span[@class="a-text-price"]/span[@class="a-offscreen"]/text()').get()

            yield {
                'title': title,
                'product_link': product_link,
                'price': price,
                'list_price': list_price
            }

        # ✅ Handle pagination
        next_page = response.xpath('//a[contains(@class, "s-pagination-next")]/@href').get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield SeleniumRequest(
                url=next_page_url,
                callback=self.parse,
                wait_time=5
            )
