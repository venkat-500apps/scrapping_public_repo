import requests
import scrapy


class flexpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["flexjobs.com"]
    start_urls = ["https://www.flexjobs.com/search?search=python+developer&location=bengaluru&latlng=17.4563197%2C78.3728344"]

    def parse(self,response,):
      
        job_links_data=response.xpath("//div[@class='container container-body excludes-search']//li/div//a").xpath('@href').getall()
        print(job_links_data)
    
        job_title=response.xpath("//a[@class='job-title job-link']/text()").getall()
        for job_name in job_title:
            print(job_name.strip())
        
        job_locations = response.xpath("//div[@class='col pe-0 job-locations text-truncate']/text()").getall()
        for location in job_locations:
            print(location.strip())

        posted_date=response.xpath("//div[@class='job-age']/text()").getall()
        for post_date in posted_date:
            print(post_date.strip())

        job_description=response.xpath("//div[@class='job-description']/text()").getall()
        for description in job_description:
            print(description.strip())
