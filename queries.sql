SELECT COUNT(*)
FROM fund_master;


SELECT fund_house,
COUNT(*)

FROM fund_master

GROUP BY fund_house;


SELECT category,

AVG(expense_ratio_pct)

FROM scheme_performance

GROUP BY category;


SELECT transaction_type,

SUM(amount_inr)

FROM investor_transactions

GROUP BY transaction_type;


SELECT risk_grade,

COUNT(*)

FROM scheme_performance

GROUP BY risk_grade;