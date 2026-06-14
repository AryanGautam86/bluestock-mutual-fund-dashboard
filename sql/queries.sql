-- Top 5 Funds by Expense Ratio

SELECT
scheme_name,
expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct DESC
LIMIT 5;


-- Number of Funds by Category

SELECT
category,
COUNT(*) AS total_funds
FROM dim_fund
GROUP BY category;


-- Average NAV

SELECT AVG(nav)
FROM fact_nav;


-- Maximum NAV

SELECT MAX(nav)
FROM fact_nav;


-- Minimum NAV

SELECT MIN(nav)
FROM fact_nav;


-- Transactions by Type

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;


-- Average Investment by State

SELECT
state,
AVG(amount_inr)
FROM fact_transactions
GROUP BY state;


-- Number of Investors

SELECT COUNT(DISTINCT investor_id)
FROM fact_transactions;


-- Funds by Risk Category

SELECT
risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;


-- Average Expense Ratio

SELECT AVG(expense_ratio_pct)
FROM dim_fund;