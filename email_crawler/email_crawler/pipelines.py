# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class EmailCrawlerPipeline:
    def process_item(self, item, spider):
        return item


class DuplicatesPipeline:
    """Drop duplicate emails in‐memory."""
    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        email = item.get("email")
        if not email:
            return item
        if email in self.seen:
            raise DropItem()
        self.seen.add(email)
        return item