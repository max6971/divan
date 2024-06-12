import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/novosibirsk/category/potolocnye-svetilniki"]

    def parse(self, response):
        svetilniki = response.css('div._Ud0k')
        for svetilnik in svetilniki:
            yield {
                'name' : svetilnik.css('div.lsooF span::text').get(),
                'price': svetilnik.css('div.q5Uds span::text').get(),
                'url': svetilnik.css('a').attrib['href']
            }