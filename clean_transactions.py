import pandas as pd

# Load dataset
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Convert date format
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Fill missing KYC values
df["kyc_status"] = (
    df["kyc_status"]
    .fillna("Unknown")
)

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Rows:", len(df))

print("Saved successfully")