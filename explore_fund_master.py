import pandas as pd

df = pd.read_csv(

    "data/raw/01_fund_master.csv"

)

print("\nUnique Fund Houses")

print(df["fund_house"].unique())

print("\nCategories")

print(df["category"].unique())

print("\nSub Categories")

print(df["sub_category"].unique())

print("\nPlans")

print(df["plan"].unique())

print("\nTotal AMFI Codes")

print(df["amfi_code"].nunique())