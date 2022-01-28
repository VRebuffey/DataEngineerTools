import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit,auth in zip(response.xpath('//div[@class="figsco__quote__text"]'),
                            response.xpath('//div[@class="figsco__fake__col-9"]')):
            text_value = cit.xpath('a/text()').extract_first()
            author_value = auth.xpath('a/text()').extract_first()
            yield { 'text' : text_value.strip('“').strip('”'),
                    'author' : author_value }         