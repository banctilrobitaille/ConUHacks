import scrapy
from IntelligentCellar.models import Bottle
from IntelligentCellar.models import Crawler

class SAQCrawler(scrapy.Spider):

    name = "SAQ"
    cup = Crawler.objects.all()[0].cup
    allowed_domains = ["saq.com"]
    start_urls = [
        "http://www.saq.com/webapp/wcs/stores/servlet/SearchDisplay?storeId=20002&catalogId=50000&"
        "langId=-2&pageSize=20&beginIndex=0&searchCategroy=Entete&searchTerm=" + cup,
    ]

    def parse(self, response):

        nom = response.xpath('//h1[@class="product-description-title"]/text()').extract_first().\
            replace('\n', ' ').replace('\r', '').encode('utf-8')

        color = response.xpath('//div[@class="product-description-title-type"]/text()').extract_first().\
            replace('\n', ' ').replace('\r', ' ').replace(' ', '').split("Vin")[1].split(",")[0].encode('utf-8')

        size = response.xpath('//div[@class="product-description-title-type"]/text()').extract_first().\
            replace('\n', ' ').replace('\r', ' ').replace(' ', '').split(",")[1].split(",")[0].encode('utf-8')

        country = response.xpath('//div[@class="product-page-subtitle"]/text()').extract_first().\
            replace('\n', '').replace('\r', '').replace(' ', '').encode('utf-8')

        region = response.xpath('//div[@class="product-description-region product-page-subtitle"]/text()').\
            extract_first().replace('\n', '').replace('\r', '').replace(' ', '').encode('utf-8')

        code_SAQ = response.xpath('//div[@class="product-description-row2"]').re(r'[0-9]{8}')[0]

        image_url = "https://s7d9.scene7.com/is/image/SAQ/" + code_SAQ + "_is?$saq%2Dprod%2Dtra$"

        print image_url
        #print response.xpath('//td[@class="product-detailsL"]/span/text()').count()

        productDetailsR = response.xpath('//td[@class="product-detailsL"]/span/text()').extract()
        productDetailsL = response.xpath('//td[@class="product-detailsR"]/span/text()').extract()

        appelationControlle = None
        alcoholDegree = None
        productor= None

        for i in range(0,len(productDetailsR)):

            if "Appellation" in productDetailsR[i]:
                appelationControlle = productDetailsL[i].\
            replace('\n', ' ').replace('\r', ' ').replace(' ', '').encode('utf-8')

            elif "alcool" in productDetailsR[i]:
                alcoholDegree = productDetailsL[i].\
            replace('\n', ' ').replace('\r', ' ').replace(' ', '').encode('utf-8')

            elif "Producteur" in productDetailsR[i]:
               productor =  productDetailsL[i].\
            replace('\n', ' ').replace('\r', ' ').encode('utf-8')


       #
       # # recipename = "\n" + "Recette : " + response.xpath('//span[@class="recipes-name"]/text()').extract()[0].\
       #  #    replace('\n', ' ').replace('\r', ' ').encode('utf-8')
       #  #print recipename
       #
       #  recipelink = response.xpath("//div[@id='recipes']/ul/li/a/@href").extract()[0]
       #  print recipelink
       #
       #  recipe2 = "\n" + "Recette : " + response.xpath('//span[@class="recipes-name"]/text()').extract()[1].\
       #      replace('\n', ' ').replace('\r', ' ').encode('utf-8')
       #  print recipe2
       #
       #  recipe3 = "\n" + "Recette : " + response.xpath('//span[@class="recipes-name"]/text()').extract()[2].\
       #      replace('\n', ' ').replace('\r', ' ').encode('utf-8')
       #  print recipe3
       #
       #  recipe4 = "\n" + "Recette : " + response.xpath('//span[@class="recipes-name"]/text()').extract()[3].\
       #      replace('\n', ' ').replace('\r', ' ').encode('utf-8')
       #  print recipe4
       #
       #  print "\n\n\n"

        b = Bottle()
        b.colour = color
        b.cup = self.cup
        b.name = nom
        b.degreeOfAlcohol = alcoholDegree
        b.producer = productor
        b.country = country
        b.regulatedDesignation = appelationControlle
        b.size = size
        b.image_url = image_url
        b.save()
