-- Primary Keys

fund_master(amfi_code)

benchmark_indices(index_name)

industry_folio_count(month)

-- Foreign Keys

nav_history.amfi_code
REFERENCES fund_master(amfi_code)

scheme_performance.amfi_code
REFERENCES fund_master(amfi_code)

investor_transactions.amfi_code
REFERENCES fund_master(amfi_code)

portfolio_holdings.amfi_code
REFERENCES fund_master(amfi_code)