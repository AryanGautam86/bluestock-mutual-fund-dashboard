import streamlit as st
from utils.database import run_query

st.title("🏠 Dashboard Overview")

st.markdown(
"""
Welcome to the **Bluestock Mutual Fund Analytics Dashboard**.

This dashboard provides insights into:

- 📈 Mutual Fund NAV
- 🏆 Fund Performance
- 👥 Investor Behaviour
- 💼 Portfolio Analysis
"""
)

st.markdown("---")

# ==========================================
# Load Data
# ==========================================

funds = run_query("SELECT * FROM dim_fund")
nav = run_query("SELECT * FROM fact_nav")
performance = run_query("SELECT * FROM fact_performance")
transactions = run_query("SELECT * FROM fact_transactions")

# ==========================================
# KPI Cards
# ==========================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Mutual Funds",
    funds["amfi_code"].nunique()
)

col2.metric(
    "Fund Houses",
    funds["fund_house"].nunique()
)

col3.metric(
    "NAV Records",
    len(nav)
)

col4.metric(
    "Investors",
    transactions["investor_id"].nunique()
)

st.markdown("---")

col5, col6, col7 = st.columns(3)

col5.metric(
    "Transactions",
    len(transactions)
)

col6.metric(
    "Avg 1-Year Return",
    f"{performance['return_1yr_pct'].mean():.2f}%"
)

col7.metric(
    "Total Investment",
    f"₹ {transactions['amount_inr'].sum():,.0f}"
)

st.markdown("---")

st.subheader("📌 Project Summary")

st.info("""
This dashboard is built using:

- Python
- SQLite
- Streamlit
- Plotly

The project enables interactive analysis of:

- NAV trends
- Mutual fund performance
- Investor behaviour
- Portfolio allocation

Use the sidebar to explore each module.
""")
import plotly.express as px

st.markdown("---")
st.subheader("📊 Dashboard Analytics")

# ==============================
# Fund Category Distribution
# ==============================

category = (
    funds
    .groupby("category", as_index=False)
    .size()
)

fig = px.pie(
    category,
    values="size",
    names="category",
    hole=0.45,
    title="Fund Category Distribution"
)

st.plotly_chart(fig, width="stretch")

# ==============================
# Top Fund Houses
# ==============================

house = (
    funds
    .groupby("fund_house", as_index=False)
    .size()
    .sort_values("size", ascending=False)
)

fig = px.bar(
    house,
    x="fund_house",
    y="size",
    color="fund_house",
    title="Funds by Fund House"
)

st.plotly_chart(fig, width="stretch")
st.markdown("---")
st.subheader("📈 NAV Trend Preview")

sample = (
    nav
    .groupby("date", as_index=False)["nav"]
    .mean()
)

fig = px.line(
    sample,
    x="date",
    y="nav",
    title="Average NAV Over Time"
)

st.plotly_chart(fig, width="stretch")
st.markdown("---")
st.subheader("💰 Transaction Types")

transaction = (
    transactions
    .groupby("transaction_type", as_index=False)
    .size()
)

fig = px.pie(
    transaction,
    values="size",
    names="transaction_type",
    hole=0.5,
    title="Transaction Distribution"
)

st.plotly_chart(fig, width="stretch")
st.markdown("---")

st.success("✔ Database Connected")

st.info(
"""
### Technologies Used

- Python
- SQLite
- Pandas
- Plotly
- Streamlit
"""
)