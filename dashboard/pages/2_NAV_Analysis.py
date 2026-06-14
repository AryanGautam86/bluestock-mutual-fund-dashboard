import streamlit as st
import plotly.express as px
from utils.database import run_query

st.title("📈 NAV Analysis")

# Load data
nav = run_query("""
SELECT *
FROM fact_nav
""")

# Convert date
nav["date"] = nav["date"].astype("datetime64[ns]")

# Sidebar filter
funds = sorted(nav["amfi_code"].unique())

selected = st.sidebar.multiselect(
    "Select Mutual Funds",
    funds,
    default=funds[:5]
)


filtered = nav[
    nav["amfi_code"].isin(selected)
]

# ===========================
# ADD THE KPI CODE HERE
# ===========================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Funds Selected",
    filtered["amfi_code"].nunique()
)

col2.metric(
    "Highest NAV",
    round(filtered["nav"].max(), 2)
)

col3.metric(
    "Average NAV",
    round(filtered["nav"].mean(), 2)
)

st.markdown("---")

# ===========================
# Continue here
# ===========================

st.subheader("Filtered NAV Data")

with st.expander("View Data"):
    st.dataframe(filtered)

st.download_button(
    "⬇ Download NAV CSV",
    filtered.to_csv(index=False),
    file_name="nav_data.csv",
    mime="text/csv"
)

st.markdown("---")

st.subheader("NAV Trend")

fig = px.line(
    filtered,
    x="date",
    y="nav",
    color="amfi_code",
    title="Daily NAV Trend"
)

st.plotly_chart(fig, use_container_width=True)