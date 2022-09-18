import scrapy
from GuardianScrapper.items import GuardianscrapperItem


class TheguardianSpider(scrapy.Spider):
    name = "TheGuardian"

    #start_urls = ['https://www.theguardian.com/international'] # tested successfull and working both (manual testing)

    # A short cut to the start_requests method, that's why we here used start_urls (official documentation : https://docs.scrapy.org/en/latest/intro/tutorial.html#:~:text=A%20shortcut%20to,%C2%B6)

    start_urls = ['https://www.theguardian.com/world/all']

    # The parse() method will be called to handle each of the requests foA
    #
    # Hr those URLs, even though we haven’t explicitly told Scrapy to do so.
    # This happens because parse() is Scrapy’s default callback method, which is called for requests without an explicitly assigned callback.


    def parse(self, response):
        ARTICLE_URL_SELECTOR = '//*[contains(@class,"fc-item__link")]//@href'
        for article_url in response.xpath(ARTICLE_URL_SELECTOR).extract():
            yield scrapy.Request(
                url=article_url,
                callback=self.parsearticle
            )

        NEXT_PAGE_SELECTOR = '//*[contains(@class,"pagination__action--static") and contains(@rel,"next")]//@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if (next_page):
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )

    def parsearticle(self, response):
        # Test if the article is already crawled
        if ('cached' in response.flags):
            return

        HEADLINE_SELECTOR = '//div[contains(@data-gu-name,"headline")]//h1//text()'
        CONTENT_SELECTOR = '//*[contains(@id,"maincontent")]//p//text()'
        AUTHOR_SELECTOR = '//a[contains(@rel,"author")]//text()'
        PUBLISHEDAT_SELECTOR = '//*[contains(@class,"dcr-")]//summary//span//text()'

        item = GuardianscrapperItem()

        item['author'] = response.xpath(AUTHOR_SELECTOR).extract_first()
        item['headline'] = response.xpath(HEADLINE_SELECTOR).extract_first()
        item['content'] = ''.join(response.xpath(CONTENT_SELECTOR).extract())
        item['url'] = response.request.url
        item['published_at'] = response.xpath(PUBLISHEDAT_SELECTOR).extract_first()

        yield item
