# Bluestock Mutual Fund Data Dictionary

## dim_fund

| Column | Description |
|---------|-------------|
| amfi_code | Unique AMFI Scheme Code |
| fund_house | Mutual Fund Company |
| scheme_name | Mutual Fund Scheme |
| category | Equity / Debt |
| sub_category | Large Cap / Mid Cap / Small Cap |
| plan | Direct / Regular |
| launch_date | Launch Date |
| benchmark | Benchmark Index |
| expense_ratio_pct | Expense Ratio (%) |
| exit_load_pct | Exit Load (%) |
| min_sip_amount | Minimum SIP Amount |
| min_lumpsum_amount | Minimum Lumpsum Amount |
| fund_manager | Fund Manager |
| risk_category | Risk Category |
| sebi_category_code | SEBI Category Code |

---

## fact_nav

Stores daily NAV values of every mutual fund.

---

## fact_transactions

Stores every investor transaction including SIP, Lumpsum and Redemption.

---

## fact_performance

Stores performance metrics of each mutual fund.