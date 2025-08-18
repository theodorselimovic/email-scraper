# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from urllib.parse import urlparse

class EmailCrawlerPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline:
    # drops duplicates and email adresses that do not correspond to company domain
    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        email = item.get("email")
        _, domain = email.lower().split("@")
        if not email:
            return item
        if email in self.seen:
            raise DropItem("Email already found")
        if domain not in spider.domains_without_www:
            raise DropItem("Email does not belong to allowed domain")
        self.seen.add(email)
        return item