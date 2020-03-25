# -*- coding: utf-8 -*-
import scrapy
import base64
import requests

class QuotesSpider(scrapy.Spider):
    name = "consulta_remedios"
    start_urls = [
        "https://consultaremedios.com.br/campanha/ofertas/c"
    ]
    

    def parse(self, response):
        remedios = []
        for quote in response.css('div.result-item'):
            yield {
                'remedio': quote.css('span::text').get(),
                'classificao': quote.css('span.result-item__classification::text').get(),
                'qtdOfertas': quote.css('span.result-item__price-label::text').get(),
                'valor': quote.css('span.result-item__price-value::text').get(),
                'linkOferta': quote.css('a.result-item__price-button::attr(href)').get(),
                'b64': base64.b64encode(requests.get(quote.css('img.result-item__image::attr(src)').extract()[1]).content).decode('utf-8')
            }            
        next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)