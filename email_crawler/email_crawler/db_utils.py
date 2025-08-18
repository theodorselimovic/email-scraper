import csv

def get_crawl_urls_csv(path, url_col="url"):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [row[url_col].strip() for row in reader if row.get(url_col)]

url_list = get_crawl_urls_csv("/Users/theodorselimovic/Library/Mobile Documents/com~apple~CloudDocs/Jobb/Ratio/outscraper_urls.csv")
