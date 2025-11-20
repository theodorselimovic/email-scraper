import csv
import os

#this looks like some really shit coding. Let's redo the function so that it asks for the absolute path to the file.
#This only works when the url columns is actually called url. 
# User should input the path, and then we should open it up, check for the url column, and then take out all the stuff. 
def get_crawl_urls_csv(path, url_col="url"):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter=";")
        return [row[url_col].strip() for row in reader if row.get(url_col)]
    
#def get_crawl_urls_csv():
   # path = input("Please type the absolute path of the csv file containing the webites you would like to crawl: ")
# #
#     if not path.endswith(".csv'"):
#         print("Incorrect path name. Make sure it ends with exactly .csv")
#         return []
    
#     # Check if file exists
#     if not os.path.exists(path):
#         print(f"File not found: {path}")
#         return []

#     with open(path, newline = "", encoding = "utf-8-sig") as csvfile: 
#         reader = csv.DictReader(csvfile, delimiter = ";")

#         try: 
#             first_row = next(reader)
#         except StopIteration:
#             print("CSV file is empty or contains only headers")
#             return[]
        
#         urls_col = None
#         for fieldnames in reader.fieldnames:
#             value = first_row.get(fieldnames).strip()
#             if value.startswith("http"):
#                 urls_col = fieldnames
#                 break

#         return [row[urls_col].strip() for row in reader if row.get(urls_col)]
    
url_list = get_crawl_urls_csv('/Users/theodorselimovic/Library/CloudStorage/OneDrive-Personal/Work/Ratio/Hemsideadresser/Hotell urls.csv')