import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Stock Market Analysis",
    page_icon="📈",
    layout="wide"
)

# =====================================================
# TITLE
# =====================================================

st.title("📈 Data Driven Stock Market Analysis")

# =====================================================
# LOAD DATA
# =====================================================

green_df = pd.read_csv("output/top_10_green_stocks.csv")
red_df = pd.read_csv("output/top_10_red_stocks.csv")

# =====================================================
# SEARCH + FILTER SECTION
# =====================================================

col1, col2 = st.columns(2)

with col1:
    search_ticker = st.text_input(
        "🔍 Search by Ticker",
        placeholder="Example: TRENT"
    )

with col2:

    sector_list = sorted(
        list(
            set(green_df["Sector"]).union(
                set(red_df["Sector"])
            )
        )
    )

    selected_sector = st.selectbox(
        "🏢 Filter by Sector",
        ["All"] + sector_list
    )

# =====================================================
# APPLY TICKER SEARCH
# =====================================================

if search_ticker:

    green_df = green_df[
        green_df["Ticker"].str.contains(
            search_ticker,
            case=False,
            na=False
        )
    ]

    red_df = red_df[
        red_df["Ticker"].str.contains(
            search_ticker,
            case=False,
            na=False
        )
    ]

# =====================================================
# APPLY SECTOR FILTER
# =====================================================

if selected_sector != "All":

    green_df = green_df[
        green_df["Sector"] == selected_sector
    ]

    red_df = red_df[
        red_df["Sector"] == selected_sector
    ]

# =====================================================
# ROUND RETURNS
# =====================================================

green_df["Yearly_Return_%"] = green_df["Yearly_Return_%"].round(2)
red_df["Yearly_Return_%"] = red_df["Yearly_Return_%"].round(2)

st.markdown("---")

# =====================================================
# DASHBOARD METRICS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🟢 Green Stocks", len(green_df))

with col2:
    st.metric("🔴 Red Stocks", len(red_df))

with col3:
    st.metric("📊 Total Stocks", len(green_df) + len(red_df))

st.markdown("---")

# =====================================================
# MARKET HIGHLIGHTS
# =====================================================

st.subheader("🏆 Market Highlights")

col1, col2 = st.columns(2)

with col1:

    if not green_df.empty:
        top_gainer = green_df.iloc[0]

        st.success("📈 Top Gainer")
        st.write(f"**Ticker:** {top_gainer['Ticker']}")
        st.write(f"**Sector:** {top_gainer['Sector']}")
        st.write(f"**Return:** {top_gainer['Yearly_Return_%']:.2f}%")
    else:
        st.warning("No Green Stocks Found")

with col2:

    if not red_df.empty:
        top_loser = red_df.iloc[0]

        st.error("📉 Top Loser")
        st.write(f"**Ticker:** {top_loser['Ticker']}")
        st.write(f"**Sector:** {top_loser['Sector']}")
        st.write(f"**Return:** {top_loser['Yearly_Return_%']:.2f}%")
    else:
        st.warning("No Red Stocks Found")

st.markdown("---")

# =====================================================
# GREEN STOCK CHART
# =====================================================

st.subheader("📈 Top Green Stocks Performance")

if not green_df.empty:

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

    st.plotly_chart(fig_green, use_container_width=True)

else:
    st.info("No Green Stocks Available")

st.markdown("---")

# =====================================================
# RED STOCK CHART
# =====================================================

st.subheader("📉 Top Red Stocks Performance")

if not red_df.empty:

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

    st.plotly_chart(fig_red, use_container_width=True)

else:
    st.info("No Red Stocks Available")

st.markdown("---")

# =====================================================
# GREEN TABLE
# =====================================================

st.subheader("🟢 Top Green Stocks")

if not green_df.empty:

    green_display = green_df.copy()

    green_display["Yearly_Return_%"] = (
        green_display["Yearly_Return_%"]
        .map(lambda x: f"{x:.2f}%")
    )

    st.dataframe(
        green_display,
        use_container_width=True
    )

else:
    st.info("No Green Stocks Found")

st.markdown("---")

# =====================================================
# RED TABLE
# =====================================================

st.subheader("🔴 Top Red Stocks")

if not red_df.empty:

    red_display = red_df.copy()

    red_display["Yearly_Return_%"] = (
        red_display["Yearly_Return_%"]
        .map(lambda x: f"{x:.2f}%")
    )

    st.dataframe(
        red_display,
        use_container_width=True
    )

else:
    st.info("No Red Stocks Found")