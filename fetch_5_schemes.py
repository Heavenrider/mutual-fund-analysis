import requests
import pandas as pd

schemes = {

    119551: "SBI Bluechip",

    120503: "ICICI Bluechip",

    118632: "Nippon Large Cap",

    119092: "Axis Bluechip",

    120841: "Kotak Bluechip"

}

results = []

for code, name in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    latest = data["data"][0]

    results.append({

        "scheme_code": code,

        "scheme_name": name,

        "date": latest["date"],

        "nav": latest["nav"]

    })

df = pd.DataFrame(results)

df.to_csv(

    "data/raw/live_nav_5_schemes.csv",

    index=False

)

print(df)

print("\nFile saved successfully.")