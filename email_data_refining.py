import glob
import pandas as pd
import json

#Reads json files and returns a pandas datafram without any duplicates
def json_reader(path_pattern):
    dfs = []
    for filepath in glob.glob(path_pattern):
            with open(filepath, "r") as f:
                data = pd.DataFrame(json.load(f))
                dfs.append(data)
    return pd.concat(dfs, ignore_index=True).drop_duplicates(subset=['email', 'source_domain'])

path_pattern = "/Users/theodorselimovic/Library/CloudStorage/OneDrive-Personal/Work/Ratio/Mejladresser/*.json"

emails = json_reader(path_pattern)

emails["email_clean"] = (emails["email"]
                         .astype(str)
                         .str.lower()
                         .str.strip()
                         .str.replace(r"u003e", "", regex=True))

emails["domain_clean"] = (
    emails["source_domain"]
    .astype(str)
    .str.lower()
    .str.strip())

#Removes a certain number of email adresses. Note parentheses
emails_clean = (
     emails[
    ~(
      (emails["email_clean"]
      .str.contains("gdpr|faktura|upphandling|rekrytering|reception|reservation|info|kontakt|support|events|bokning|restaurang|restaurant|offert|kansli|hantverkare|renovera|jobb|felanmmalan|uppsagning|press",
                     case=False,
                       na=False)) |
     ~(emails["email_clean"].str.contains(r"^[^@]+\.[^@]+@[^@]+$", regex= True))
    )
]
.drop(columns="email")
)

print(emails_clean.head())
print(len(emails_clean))

#To Do: Save the emails, presumably as a json file or something. Depends on the email sender.
emails_clean.to_csv("/Users/theodorselimovic/Library/CloudStorage/OneDrive-Personal/Work/Ratio/Mejladresser/email_clean.csv")