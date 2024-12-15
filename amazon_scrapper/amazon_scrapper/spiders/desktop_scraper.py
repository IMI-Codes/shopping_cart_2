import scrapy


class DesktopScraperSpider(scrapy.Spider):
    name = "laptop_scraper"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?k=laptops&_encoding=UTF8&content-id=amzn1.sym.1d3b8f55-c47a-4b7f-a127-3409d1ca6dd1&pd_rd_r=618b2ea5-aabc-465b-89e5-8c72ddbba465&pd_rd_w=vm9Zw&pd_rd_wg=RPNzP&pf_rd_p=1d3b8f55-c47a-4b7f-a127-3409d1ca6dd1&pf_rd_r=HFB22S4TF1PWW3VH60GV&ref=pd_hp_d_btf_unk"]

    def parse(self, response): # type: ignore
        laptops = response.css(".puisg-col-inner")
        
        #laptop_name_specs = xpath(//a//h2//span/text()').get()
        # modifications needed laptop_price = laptop.xpath('//span[contains(@class, "a-offscreen")]/text()').get()
        # review_count
        #stars = laptop.xpath('//i[span[@class="a-icon-alt"]]/span/text()').get()
        
        