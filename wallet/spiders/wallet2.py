import scrapy
import json

class Wallet2Spider(scrapy.Spider):
    name = 'wallet2'

    headers = {
          'authority': 'wallethub.com',
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/json;charset=UTF-8',
          'cookie': 'ctr_su=/search/?s=American+Express; __whid=168084928696211022438; site_id=c2b4c2b4-b9c0-4995-b0ee-f3b9928a1deb; testid=70; utm_vars=%7B%7D; _ga=GA1.2.1906327706.1680849279; _gid=GA1.2.2128081781.1680849279; wh_noad=Yes; base=427d4c0c.5f8bc01804ffc; AMP_TOKEN=%24NOT_FOUND; XSRF-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjbGllbnRfaWQiOiIxNjgwODQ5Mjg2OTYyMTEwMjI0MzgiLCJpYXQiOjE2ODA4NjE3MjUsImV4cCI6MTY4MDg2NTMzMCwicmF5IjoiN2I0MTZlZjM4ZTU3ODU3NS1CT00ifQ.3dhpDhua9gmV73id8v4ExBN83AckdRWniM68EfyeEbg',
          'referer': 'https://wallethub.com/profile/american-express-13000208i',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
        }

    def start_requests(self):
        
        url = "https://wallethub.com/ajax.php?action=Reviews.GetForPage&p=1&sort_by=dtdn&uid=13000208"
        
        

        yield scrapy.Request(url,
                            method="GET",
                            meta={'counter_page':1, "count" : 0,},
                            headers=self.headers,  
                            callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.text)
        # print(json_data)

        for i in json_data['reviews']:
            try:
                user_id = i['user_id']
            except:
                user_id = None
            try:    
                user_avatar = i['user_avatar']
            except:
                user_avatar = None
            try:    
                user_handle = i['user_handle']
            except:
                user_handle = None
            try:    
                content = i['content']
            except:
                content = None
            try:
                total_comments = i['total_comments']
            except:
                total_comments = None
            try:    
                date = i['date']
            except:
                date = None
            try:    
                rating = i['rating']
            except:
                rating = None
            try:
                department = i['department']
            except:
                department = None
            try:    
                department_link = i['department_link']
            except:
                department_link = None
            try:
                inst_name = i['inst_name']
            except:
                inst_name = None
            try:    
                inst_department = i['inst_department']
            except:
                inst_department = None


            item = {
                    "user_id":user_id,
                    "user_avatar":user_avatar,
                    "user_handle":user_handle,
                    "content":content,
                    "total_comments":total_comments,
                    "date":date,
                    "rating":rating,
                    "department":department,
                    "department_link":department_link,
                    "inst_name":inst_name,
                    "inst_department":inst_department
            }
            yield item
        
        if response.meta['counter_page'] < 305:
            response.meta['counter_page']+= 1
            url = f"https://wallethub.com/ajax.php?action=Reviews.GetForPage&p={response.meta['counter_page']}&sort_by=dtdn&uid=13000208"
            
            yield scrapy.Request(   url,
                                    method="GET",
                                    meta={"url":url,'counter_page':response.meta['counter_page']},
                                    callback=self.parse,
                                    headers=self.headers,                                        
                                    dont_filter=True    
                                )    


