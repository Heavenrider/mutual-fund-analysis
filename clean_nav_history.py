import pandas as pd

df = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

# convert date
df["date"] = pd.to_datetime(
    df["date"]
)

# sort
df = df.sort_values(
    by=["amfi_code", "date"]
)

# forward fill NAV
df["nav"] = df.groupby(
    "amfi_code"
)["nav"].ffill()

# remove duplicates
df = df.drop_duplicates()

# NAV must be > 0
df = df[df["nav"] > 0]

# save

df.to_csv(

    "data/processed/nav_history_clean.csv",

    index=False

)

print(df.shape)

print("Saved successfully")