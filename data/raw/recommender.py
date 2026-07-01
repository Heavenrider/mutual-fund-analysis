import pandas as pd

funds = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

risk = input(
    "Enter Risk Level (Low/Moderate/High): "
)

if risk.lower() == "low":

    result = funds[
        funds['risk_grade']
        .str.contains(
            "low",
            case=False,
            na=False
        )
    ]

elif risk.lower() == "moderate":

    result = funds[
        funds['risk_grade']
        .str.contains(
            "moderate",
            case=False,
            na=False
        )
    ]

else:

    result = funds[
        funds['risk_grade']
        .str.contains(
            "high",
            case=False,
            na=False
        )
    ]

result = result.sort_values(
    'sharpe_ratio',
    ascending=False
)

print(
    result[
        [
            'scheme_name',
            'risk_grade',
            'sharpe_ratio'
        ]
    ].head(3)
)