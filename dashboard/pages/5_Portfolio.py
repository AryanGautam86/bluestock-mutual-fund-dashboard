import streamlit as st
import plotly.express as px
from utils.database import run_query

st.title("💼 Portfolio Analysis")

# ==========================================
# Load Data
# ==========================================

portfolio = run_query("""
SELECT *
FROM fact_transactions
""")

# ==========================================
# Sidebar Filter
# ==========================================

funds = sorted(portfolio["amfi_code"].unique())

selected_funds = st.sidebar.multiselect(
    "Select Fund",
    funds,
    default=funds[:5]
)

filtered = portfolio[
    portfolio["amfi_code"].isin(selected_funds)
]

# ==========================================
# KPI Cards
# ==========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Selected Funds",
    filtered["amfi_code"].nunique()
)

col2.metric(
    "Total Investment",
    f"₹ {filtered['amount_inr'].sum():,.0f}"
)

col3.metric(
    "Average Investment",
    f"₹ {filtered['amount_inr'].mean():,.0f}"
)

st.markdown("---")

# ==========================================
# Dataset
# ==========================================

st.subheader("📋 Portfolio Data")

with st.expander("View Portfolio"):
    st.dataframe(filtered)
st.download_button(
    "⬇ Download Portfolio CSV",
    filtered.to_csv(index=False),
    file_name="portfolio.csv",
    mime="text/csv"
)

# ==========================================
# Investment by Fund
# ==========================================

st.markdown("---")
st.subheader("📊 Investment by Fund")

fund = (
    filtered
    .groupby("amfi_code", as_index=False)["amount_inr"]
    .sum()
)

fig = px.bar(
    fund,
    x="amfi_code",
    y="amount_inr",
    color="amfi_code",
    title="Investment by Fund"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Transaction Type
# ==========================================

st.markdown("---")
st.subheader("💳 Transaction Type")

trans = (
    filtered
    .groupby("transaction_type", as_index=False)
    .size()
)

fig = px.pie(
    trans,
    values="size",
    names="transaction_type",
    hole=0.45,
    title="Transaction Types"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Investment by State
# ==========================================

st.markdown("---")
st.subheader("🗺️ Investment by State")

state = (
    filtered
    .groupby("state", as_index=False)["amount_inr"]
    .sum()
)

fig = px.bar(
    state,
    x="state",
    y="amount_inr",
    color="state",
    title="Investment by State"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Investment Timeline
# ==========================================

st.markdown("---")
st.subheader("📈 Investment Timeline")

timeline = (
    filtered
    .groupby("transaction_date", as_index=False)["amount_inr"]
    .sum()
)

fig = px.line(
    timeline,
    x="transaction_date",
    y="amount_inr",
    markers=True,
    title="Daily Investments"
)

st.plotly_chart(fig, use_container_width=True)