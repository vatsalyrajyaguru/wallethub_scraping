# from datetime import datetime, timedelta
# import math
# import scrapy

# class FlyertalkDataSpider(scrapy.Spider):
#     name = 'flyertalk_data'

#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
#         }
        
#     def __init__(self,input, **kwargs):
#         super().__init__(**kwargs)
#         self.input = input
#         self.keyword = input.get("keyword")
#         self.proxy = input.get("proxy")
#         self.from_date = datetime.strptime(self.input['from_date'],"%Y-%m-%d").date() if self.input.get('from_date') else datetime.strptime("1900-01-01","%Y-%m-%d").date()
#         self.max_record = input.get("no_of_urls",0)
    
#     def start_requests(self):

#             url = f"https://www.flyertalk.com/forum/search.php?do=process&query={self.keyword}&pp=25"   
#             yield scrapy.Request(   url,
#                                     method="GET",
#                                     meta={"url":url,'currunt_page': 1,"keyword":self.keyword,"count" : 0 },
#                                     callback=self.parse,
#                                     headers=self.headers,                                    
#                                     dont_filter=True    
#                                     )

#     def parse(self, response):

#         total_page = math.ceil(int(response.xpath('//div[@class="iblock smallfont text-left"]/text()').get().split("of")[1].split("Search")[0].strip())/25)

#         for i in response.xpath('//div[@id="threadslist"]//div[@class="trow text-center"]'):
#             try:
#                 title = i.xpath('.//h4/a/text()').get()
#             except:
#                 title = None
#             try:
#                 url = "https://www.flyertalk.com/forum/" + i.xpath('.//h4/a/@href').get()
#             except:
#                 url = None
#             try:
#                 author_name = i.xpath('.//div[contains(@id,"td_threadtitle")]/div[2]/span[1]/text()').get().strip()
#             except:
#                 author_name = None
#             try:
#                 author_url = "https://www.flyertalk.com/forum/" + i.xpath('.//div[contains(@id,"td_threadtitle")]/div[2]/span/@onclick').get().strip().split("open('")[1].split("',")[0]
#             except:
#                 author_url = None
#             try:
#                 post_dates = i.xpath('.//div[contains(@id,"td_threadtitle")]/div[2]/span[2]/text()').get().replace("on","").strip()
#                 if "Today" in post_dates:
#                     post_date = str(datetime.today().date())
#                 elif "Yesterday" in post_dates:
#                     post_date = str(datetime.today().date()  - timedelta(days=1))
#                 else:
#                     post_date = str(datetime.strptime(post_dates, "%b %d, %y").date())
#             except:
#                 post_date = None
                
#             try:
#                 last_post_dates = i.xpath('.//div[@class="tcell alt2 smallfont"]/div/text()[1]').get().strip()
#                 if "Today" in last_post_dates:
#                     last_post_date = str(datetime.today().date())
#                 elif "Yesterday" in last_post_dates:
#                     last_post_date = str(datetime.today().date()  - timedelta(days=1))
#                 else:
#                     last_post_date = str(datetime.strptime(last_post_dates, "%b %d, %y").date())
#             except:
#                 last_post_date = None
#             try:
#                 last_post_author_name = i.xpath('.//div[@class="tcell alt2 smallfont"]/div/a/text()').get().strip()
#             except:
#                 last_post_author_name = None
#             try:
#                 last_post_author_url = "https://www.flyertalk.com/forum/" + i.xpath('.//div[@class="tcell alt2 smallfont"]/div/a[1]/@href').get().strip()
#             except:
#                 last_post_author_url = None
#             try:
#                 last_post_details_url = "https://www.flyertalk.com/forum/" + i.xpath('.//div[@class="tcell alt2 smallfont"]/div/a[2]/@href').get().strip()
#             except:
#                 last_post_details_url = None
#             try:
#                 no_of_reviews = int(i.xpath('.//div[@class="tcell alt1"]/a/text()').get())
#             except:
#                 no_of_reviews = 0
#             try:
#                 reviews_url = "https://www.flyertalk.com/forum/" + i.xpath(".//div[@class='tcell alt1']/a/@href").get()
#             except:
#                 reviews_url = None
#             try:
#                 post_view = i.xpath('.//div[@class="tcell alt1"]/span/text()').get()
#             except:
#                 post_view = None
#             try:
#                 forum = i.xpath('.//div[@class="tcell alt1 text-left"]/a/text()').get()
#             except:
#                 forum = None
#             try:
#                 forum_url = "https://www.flyertalk.com/forum/" + i.xpath('.//div[@class="tcell alt1 text-left"]/a/@href').get()
#             except:
#                 forum_url = None
            
#             if self.from_date < datetime.strptime(str(post_date), "%Y-%m-%d").date():
#                 if not self.max_record or self.max_record > response.meta['count'] :
#                     response.meta['count'] += 1
#                     yield {
#                             "input_details" : self.input,
#                             "data_type" : "post",
#                             "name" : title,
#                             "url" : url,
#                             "author_name" : author_name,
#                             "author_url" : author_url,               
#                             "post_date" : post_date,
#                             "no_of_reviews" : no_of_reviews,
#                             "scrape_time":str(datetime.today().date()),
#                             "aux_info" : {                                
#                                     "reviews_url" : reviews_url,
#                                     "post_view" : post_view,
#                                     "forum" : forum,
#                                     "forum_url" : forum_url,
#                                     "last_post_date" : last_post_date,
#                                     "last_post_author_name" : last_post_author_name,
#                                     "last_post_author_url" : last_post_author_url,
#                                     "last_post_details_url" : last_post_details_url
#                                     }                  
#                         }
                               
#         if response.meta['currunt_page'] < total_page:
#             response.meta['currunt_page']+= 1
#             if not self.max_record or self.max_record > response.meta['count'] :
#                 url = f"https://www.flyertalk.com/forum/search.php?do=process&query=airport&pp=25&page={response.meta['currunt_page']}"           
#                 yield scrapy.Request(   url,
#                                         method="POST",
#                                         meta={"url":url,'currunt_page': response.meta['currunt_page'],"count" : response.meta['count']},
#                                         callback=self.parse,
#                                         headers=self.headers,                                        
#                                         dont_filter=True    
#                                     )
           

