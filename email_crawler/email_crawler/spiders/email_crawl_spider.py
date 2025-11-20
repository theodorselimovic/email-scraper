# email_crawl_spider.py
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..db_utils import url_list
from urllib.parse import urlparse

#Jag har tagit bort bokahem.se för att den hade alldeles för många sidor, men man kan typ göra en separat 
# spider bara för den. Finns nog en enorm mängd mejladresser där.

class EmailCrawlSpider(CrawlSpider):
    name            = "email_crawl_spider"
    start_urls = url_list
    #This also feels inefficient. Why can't we do this in the db_utils.py function?
    allowed_domains = [urlparse(u).netloc for u in url_list]
    #Denna går in i item pipeline och bestämmer vilka mejladresser som faktiskt tas med.
    # Man kan alltså mecka med detta. T.ex lägg till @gmail.com för det kommer inte ett seriöst företag ha
    domains_without_www = [x[4:] if x.startswith("www.") else x for x in allowed_domains]
    rules = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                deny_extensions=["png","jpg","gif","css","js","pdf"]
            ),
            callback="parse_email",
            follow=True,
        ),
    )

    email_pattern = re.compile(
        r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", re.I
    )

    def parse_email(self, response):
        """
        Called on every page matched by your Rule.
        Finds all emails in the HTML and yields items.
        """
        depth = response.meta.get("depth", 0)
        self.logger.debug(f"[depth={depth}] parsing {response.url}")
        text = response.text or ""
        found = set(self.email_pattern.findall(text))

        self.logger.debug(f"{response.url} → {len(found)} emails")

        for email in found:
            domain = urlparse(response.url).netloc
            yield {
                "email":        email.lower(),
                "source_url":    response.url,
                "source_domain": domain[4:] if domain.startswith("www.") else domain 
            }