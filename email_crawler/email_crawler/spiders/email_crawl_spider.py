# email_crawl_spider.py
import re
from scrapy.exceptions import DropItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class EmailCrawlSpider(CrawlSpider):
    name            = "email_crawl_spider"
    allowed_domains = ["tagforetagen.se"]          # restricts crawling to this domain
    start_urls      = ["https://www.tagforetagen.se/"] # your seed URL(s)

    # 1. Define how links are followed
    rules = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                deny_extensions=["png","jpg","gif","css","js","pdf"]
            ),
            callback="parse_email",  # called on every fetched page
            follow=False             # keep following links from those pages
        ),
    )

    email_pattern = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}")

    def parse_email(self, response):
        found = set(self.email_pattern.findall(response.text))
        for email in found:
            yield {"email": email}


# resultat från dagens arbete: 
    # 1. Det tar lång tid att gå igenom en ordentlig hemsida.
    # Det tog säkert runt 20-30 sekunder för att gå igenom en hel webbplats med alla sina sidor.
    # 2. Går man igenom en hel webbplats, åtminstone en med många sidor, får man jävligt många mejladresser, varav endast ett fåtal är användbara.
    # Man måste alltså på något sätt begränsa vilka mejladresser som tas med, förslagsvis endast de som har samma slut som namnet på företaget. 
    # 3. I och med att man får så många behöver man kanske inte fånga upp alla avvikande fall, vilket skulle spara rejält med tid och arbete.
    # Åtminstone om man kan samla på sig många hemsidor, vilket borde vara möjligt med google maps scraping. 