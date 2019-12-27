import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/page/1/']

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css('.text::text').get()
            author = quote.css('.author::text').get()
            tags = quote.css('.tag::text').getall()
            yield {"text":text, "author":author, "tags":tags}
    
        # next_page = response.css('.next a::attr(href)').get()
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(url=next_page, callback=self.parse)
        yield response.follow(response.css('.next a')[0], callback=self.parse)