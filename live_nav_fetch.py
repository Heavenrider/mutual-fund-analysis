import requests
import pandas as pd

# HDFC Top 100 Direct
url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("Scheme Name:")

print(data["meta"]["scheme_name"])

df = pd.DataFrame(data["data"])

df.to_csv(

    "data/raw/live_nav_hdfc.csv",

    index=False

)

print("\nSaved successfully")

print(df.head())