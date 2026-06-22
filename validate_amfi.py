import pandas as pd

master = pd.read_csv(

    "data/raw/01_fund_master.csv"

)

nav = pd.read_csv(

    "data/raw/02_nav_history.csv"

)

master_codes = set(

    master["amfi_code"]

)

nav_codes = set(

    nav["amfi_code"]

)

missing = master_codes - nav_codes

extra = nav_codes - master_codes

print("\nMissing codes in NAV:")

print(len(missing))

print(missing)

print("\nExtra codes in NAV:")

print(len(extra))

print(extra)

if len(missing) == 0:

    print("\n✅ All AMFI codes validated")

else:

    print("\n⚠ Some AMFI codes are missing")