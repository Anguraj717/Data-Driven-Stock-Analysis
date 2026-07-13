import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Stock Market Analysis",
    page_icon="📈",
    layout="wide"
)

# -------------------------------
# Load CSV Files
# -------------------------------
green_df = pd.read_csv("output/top_10_green_stocks.csv")
red_df = pd.read_csv("output/top_10_red_stocks.csv")

green_df = pd.read_csv("output/top_10_green_stocks.csv")
red_df = pd.read_csv("output/top_10_red_stocks.csv")

# -------------------------------
# Top Gainer & Top Loser
# -------------------------------
top_gainer = green_df.iloc[0]
top_loser = red_df.iloc[0]

# -------------------------------
# Title
# -------------------------------
st.title("📈 Data Driven Stock Market Analysis")

st.markdown("---")

# -------------------------------
# Dashboard Metrics
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🟢 Green Stocks", len(green_df))

with col2:
    st.metric("🔴 Red Stocks", len(red_df))

with col3:
    st.metric("📊 Total Stocks", len(green_df) + len(red_df))

st.markdown("---")

# -------------------------------
# Market Highlights
# -------------------------------
st.subheader("🏆 Market Highlights")

col1, col2 = st.columns(2)

with col1:
    st.success("📈 Top Gainer")
    st.write(f"**Ticker:** {top_gainer['Ticker']}")
    st.write(f"**Sector:** {top_gainer['Sector']}")
    st.write(f"**Return:** {top_gainer['Yearly_Return_%']:.2f}%")

with col2:
    st.error("📉 Top Loser")
    st.write(f"**Ticker:** {top_loser['Ticker']}")
    st.write(f"**Sector:** {top_loser['Sector']}")
    st.write(f"**Return:** {top_loser['Yearly_Return_%']:.2f}%")

st.markdown("---")

st.subheader("📊 Top 10 Green Stocks Performance")

fig_green = px.bar(
    green_df,
    x="Ticker",
    y="Yearly_Return_%",
    color="Sector",
    title="Top Green Stocks",
    text_auto=".2f"
)

fig_green.update_layout(
    xaxis_tickangle=-45,
    height=500
)

st.plotly_chart(fig_green, width="stretch")
st.markdown("---")

st.subheader("📉 Top 10 Red Stocks Performance")

fig_red = px.bar(
    red_df,
    x="Ticker",
    y="Yearly_Return_%",
    color="Sector",
    title="Top Red Stocks",
    text_auto=".2f"
)

fig_red.update_layout(
    xaxis_tickangle=-45,
    height=500
)

st.plotly_chart(fig_red, width="stretch")

# -------------------------------
# Top 10 Green Stocks
# -------------------------------
st.subheader("🟢 Top 10 Green Stocks")
green_display = green_df.copy()
green_display["Yearly_Return_%"] = green_display["Yearly_Return_%"].map(lambda x: f"{x:.2f}%")

st.dataframe(green_display, width="stretch")

st.markdown("---")

# -------------------------------
# Top 10 Red Stocks
# -------------------------------
st.subheader("🔴 Top 10 Red Stocks")
red_display = red_df.copy()
red_display["Yearly_Return_%"] = red_display["Yearly_Return_%"].map(lambda x: f"{x:.2f}%")

st.dataframe(red_display, width="stretch")