import streamlit as st
import plotly.express as px
from utils.database import run_query

st.title("👥 Investor Analysis")

# ==========================================
# Load Data
# ==========================================

investors = run_query("""
SELECT *
FROM fact_transactions
""")

# ==========================================
# Sidebar Filter
# ==========================================

states = sorted(investors["state"].dropna().unique())

selected_states = st.sidebar.multiselect(
    "Select State",
    states,
    default=states
)

filtered = investors[
    investors["state"].isin(selected_states)
]

# ==========================================
# KPI Cards
# ==========================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Investors",
    filtered["investor_id"].nunique()
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

st.subheader("📋 Investor Transactions")

with st.expander("View Data"):
    st.dataframe(filtered)
st.download_button(
    "⬇ Download Investor CSV",
    filtered.to_csv(index=False),
    file_name="investor_data.csv",
    mime="text/csv"
)

# ==========================================
# Gender Distribution
# ==========================================

st.markdown("---")
st.subheader("🚻 Gender Distribution")

gender = filtered.groupby("gender").size().reset_index(name="count")

fig = px.pie(
    gender,
    values="count",
    names="gender",
    hole=0.45,
    title="Gender Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Age Group Distribution
# ==========================================

st.markdown("---")
st.subheader("🎂 Age Group Distribution")

age = filtered.groupby("age_group").size().reset_index(name="count")

fig = px.bar(
    age,
    x="age_group",
    y="count",
    color="age_group",
    title="Investors by Age Group"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# State-wise Investors
# ==========================================

st.markdown("---")
st.subheader("🗺️ Investors by State")

state = filtered.groupby("state").size().reset_index(name="count")

fig = px.bar(
    state,
    x="state",
    y="count",
    color="state",
    title="State-wise Investors"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# City Tier Distribution
# ==========================================

st.markdown("---")
st.subheader("🏙️ City Tier Distribution")

tier = filtered.groupby("city_tier").size().reset_index(name="count")

fig = px.pie(
    tier,
    values="count",
    names="city_tier",
    hole=0.45,
    title="City Tier Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# Payment Mode
# ==========================================

st.markdown("---")
st.subheader("💳 Payment Mode")

payment = filtered.groupby("payment_mode").size().reset_index(name="count")

fig = px.bar(
    payment,
    x="payment_mode",
    y="count",
    color="payment_mode",
    title="Payment Modes"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================
# KYC Status
# ==========================================

st.markdown("---")
st.subheader("✅ KYC Status")

kyc = filtered.groupby("kyc_status").size().reset_index(name="count")

fig = px.pie(
    kyc,
    values="count",
    names="kyc_status",
    hole=0.45,
    title="KYC Status"
)

st.plotly_chart(fig, use_container_width=True)