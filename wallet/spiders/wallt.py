import scrapy

class WalltSpider(scrapy.Spider):
    name = 'wallt'
    
    def start_requests(self):
        url = "https://wallethub.com/search/?s=American+Express"
     
        headers = {
          'authority': 'wallethub.com',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'en-US,en;q=0.9',
          'cache-control': 'max-age=0',
          'cookie': 'testcookie=1; ctr_su=/search/?s=American+Express; base=d4d27dae.5f8b9388edd6f; __whid=168084928696211022438; site_id=c2b4c2b4-b9c0-4995-b0ee-f3b9928a1deb; testid=70; utm_vars=%7B%7D; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.1906327706.1680849279; _gid=GA1.2.2128081781.1680849279; wh_noad=Yes; XSRF-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiIxNjgwODQ5Mjg2OTYyMTEwMjI0MzgiLCJpYXQiOjE2ODA4NTAxNjQsImV4cCI6MTY4MDg1Mzc2OSwicmF5IjoiN2I0MDU0Yjk3ZjIzZjQ4NC1CT00ifQ.9S1p3WGVDlx55lwAYUAXvFK-KQ4bxM578v04lLg4qvs',
          'upgrade-insecure-requests': '1',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }
        yield scrapy.Request(url, 
                             method="GET", 
                             headers=headers,  
                             callback=self.parse)
        
    def parse(self, response):
       
        for i in response.xpath("//input[contains(@class,'companypage')]//following-sibling::div"):
            tittle = i.xpath(".//a/text()").get()
            box_type = i.xpath(".//span[contains(@class,'box-type')]/text()").get()
                      
            tittle_link = f'https://wallethub.com{i.xpath(".//a//@href").get()}'

            img_link = i.xpath(".//img//@src").get()
            review = i.xpath(".//span[contains(@class,'rev-count')]/text()").get()
            address = i.xpath(".//address/text()").get()
            address_code = i.xpath(".//address/span/text()").get()
            
            item ={
                "tittle":tittle,
                "box_type":box_type,
                "tittle_link2":tittle_link,
                "img_link":img_link,
                "review":review,
                "address":address,
                "address_code":address_code
            }
            yield item

