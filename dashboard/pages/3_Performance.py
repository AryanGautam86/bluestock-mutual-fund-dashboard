import streamlit as st
import plotly.express as px
from utils.database import run_query

st.title("🏆 Fund Performance Analysis")

# -------------------------------
# Load Performance Data
# -------------------------------

performance = run_query("""
SELECT *
FROM fact_performance
""")

# -------------------------------
# Sidebar Filters
# -------------------------------

categories = sorted(performance["category"].dropna().unique())

selected_categories = st.sidebar.multiselect(
    "Select Category",
    categories,
    default=categories
)

filtered = performance[
    performance["category"].isin(selected_categories)
]

# -------------------------------
# KPI Cards
# -------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Funds",
    filtered["amfi_code"].nunique()
)

col2.metric(
    "Highest 1-Year Return",
    round(filtered["return_1yr_pct"].max(), 2)
)

col3.metric(
    "Average 1-Year Return",
    round(filtered["return_1yr_pct"].mean(), 2)
)

st.markdown("---")

# -------------------------------
# Data Table
# -------------------------------

st.subheader("📋 Performance Dataset")

with st.expander("View Performance Data"):
    st.dataframe(filtered)
st.download_button(
    "⬇ Download Performance CSV",
    filtered.to_csv(index=False),
    file_name="performance.csv",
    mime="text/csv"
)

# -------------------------------
# Top 10 Funds
# -------------------------------

st.markdown("---")
st.subheader("🏅 Top 10 Performing Funds")

top10 = (
    filtered
    .sort_values("return_1yr_pct", ascending=False)
    .head(10)
)

fig = px.bar(
    top10,
    x="return_1yr_pct",
    y="scheme_name",
    color="fund_house",
    orientation="h",
    title="Top 10 Funds by 1-Year Return"
)

fig.update_layout(
    yaxis={"categoryorder": "total ascending"}
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Average Return by Category
# -------------------------------

st.markdown("---")
st.subheader("📊 Category-wise Average Return")

avg_category = (
    filtered
    .groupby("category", as_index=False)["return_1yr_pct"]
    .mean()
)

fig = px.bar(
    avg_category,
    x="category",
    y="return_1yr_pct",
    color="category",
    title="Average 1-Year Return by Category"
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------
# Average Return by Fund House
# -------------------------------

st.markdown("---")
st.subheader("🏢 Fund House Comparison")

avg_house = (
    filtered
    .groupby("fund_house", as_index=False)["return_1yr_pct"]
    .mean()
)

fig = px.bar(
    avg_house,
    x="fund_house",
    y="return_1yr_pct",
    color="fund_house",
    title="Average Return by Fund House"
)

st.plotly_chart(fig, use_container_width=True)