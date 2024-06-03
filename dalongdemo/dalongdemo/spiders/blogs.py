from pathlib import Path

import uuid
import scrapy

import json

from dalongdemo.items import DalongdemoItem


class BlogsSpider(scrapy.Spider):
    name = "blogs"
    id =  uuid.uuid1()
    def start_requests(self):

        urls = [
            "https://cnblogs.com/rongfengliang"
        ]

        for url in urls:
            options = {
                "url": url,
                "gotoOptions": {
                    "waitUntil": "networkidle0"
                }
            }
            yield scrapy.Request(
                url="http://localhost:3000/content?token=6R0W53R135510",
                method='POST',
                dont_filter=True,
                headers={"Content-Type": "application/json"},
                body=json.dumps(options),
                callback=self.parse
            )

    def parse(self, response):
        for item in response.css("div.post"):
            dalongItem = DalongdemoItem()
            dalongItem["title"] = item.css("div.post .postTitle2 > span").get()
            dalongItem["content"] = item.css("div.postbody .c_b_p_desc").get()
            yield dalongItem
