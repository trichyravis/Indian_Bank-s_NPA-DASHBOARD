"""
STEP 6: STREAMLIT DASHBOARD - Interactive web application
===========================================================
Author: Prof. V. Ravichandran
Project: NPA Analysis Dashboard
Date: January 18, 2026

Pages:
1. Overview - System-wide KPIs and trends
2. Bank Deep Dive - Individual bank 12-quarter analysis
3. Peer Compare - Rankings and quadrant view
4. Data & Sources - Download CSV + source attribution

Run with:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ===== PAGE CONFIGURATION =====
st.set_page_config(
    page_title="NPA Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== LOAD DATA =====
@st.cache_data
def load_data():
    """Load validated data"""
    try:
        df = pd.read_csv('bank_metrics_validated.csv')
        return df
    except FileNotFoundError:
        return pd.DataFrame()

# ===== THEME & STYLING =====
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
df = load_data()

if len(df) == 0:
    st.error("❌ No data found. Please run steps 1-5 first.")
    st.stop()

# ===== SIDEBAR NAVIGATION =====
st.sidebar.title("📊 NPA Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Page:",
    ["📈 Overview", "🏦 Bank Deep Dive", "🏆 Peer Compare", "📚 Data & Sources"]
)

st.sidebar.markdown("---")
st.sidebar.info(f"📌 Data: {len(df)} rows | Banks: {df['bank'].nunique()} | "
                f"Latest: {df['period'].max()}")

# ===== PAGE 1: OVERVIEW =====
if page == "📈 Overview":
    st.title("📊 NPA Analysis Dashboard - System Overview")
    st.markdown("*Source: NSE/BSE filings | Last updated: 2026-01-18*")
    
    # Get latest period data
    latest_period = df['period'].max()
    latest_data = df[df['period'] == latest_period]
    
    if len(latest_data) == 0:
        st.warning("No data for latest period")
    else:
        # KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            avg_gnpa = latest_data['gnpa_pct'].mean()
            st.metric("🔴 Avg GNPA%", f"{avg_gnpa:.2f}%", 
                     delta=None, help="Gross NPA percentage")
        
        with col2:
            avg_nnpa = latest_data['nnpa_pct'].mean()
            st.metric("🟡 Avg NNPA%", f"{avg_nnpa:.2f}%",
                     delta=None, help="Net NPA percentage")
        
        with col3:
            avg_nim = latest_data['nim_pct'].mean()
            st.metric("💰 Avg NIM%", f"{avg_nim:.2f}%",
                     delta=None, help="Net Interest Margin")
        
        with col4:
            avg_casa = latest_data['casa_pct'].mean()
            st.metric("🏦 Avg CASA%", f"{avg_casa:.2f}%",
                     delta=None, help="Current Account Saving Account")
        
        # Rankings
        st.subheader("📌 Latest Quarter Rankings")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Lowest GNPA% (Best)**")
            gnpa_low = latest_data.nsmallest(5, 'gnpa_pct')[['bank', 'gnpa_pct']]
            st.dataframe(gnpa_low, use_container_width=True)
        
        with col2:
            st.write("**Highest NIM% (Best)**")
            nim_high = latest_data.nlargest(5, 'nim_pct')[['bank', 'nim_pct']]
            st.dataframe(nim_high, use_container_width=True)
        
        # System trend
        st.subheader("📈 System Trends")
        
        periods = df['period'].unique()[:min(4, len(df['period'].unique()))]
        trend_data = df[df['period'].isin(periods)].groupby('period').agg({
            'gnpa_pct': 'mean',
            'nim_pct': 'mean'
        }).reset_index()
        
        fig_trend = px.line(
            trend_data, 
            x='period', 
            y=['gnpa_pct', 'nim_pct'],
            markers=True,
            title="Average GNPA% and NIM% Trend",
            labels={'gnpa_pct': 'Avg GNPA%', 'nim_pct': 'Avg NIM%'},
            line_shape='linear'
        )
        st.plotly_chart(fig_trend, use_container_width=True)

# ===== PAGE 2: BANK DEEP DIVE =====
elif page == "🏦 Bank Deep Dive":
    st.title("🏦 Bank Deep Dive Analysis")
    
    # Bank selector
    selected_bank = st.selectbox("Select Bank:", sorted(df['bank'].unique()))
    
    bank_data = df[df['bank'] == selected_bank].sort_values('period')
    
    if len(bank_data) > 0:
        # Latest metrics
        latest = bank_data.iloc[-1]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("GNPA%", f"{latest['gnpa_pct']:.2f}%")
        with col2:
            st.metric("NNPA%", f"{latest['nnpa_pct']:.2f}%")
        with col3:
            st.metric("NIM%", f"{latest['nim_pct']:.2f}%")
        with col4:
            st.metric("CASA%", f"{latest['casa_pct']:.2f}%")
        
        # NPA Trend
        fig_npa = px.line(
            bank_data,
            x='period',
            y=['gnpa_pct', 'nnpa_pct'],
            markers=True,
            title=f"{selected_bank} - NPA Trend",
            labels={'gnpa_pct': 'GNPA%', 'nnpa_pct': 'NNPA%'}
        )
        st.plotly_chart(fig_npa, use_container_width=True)
        
        # Profitability
        fig_prof = px.line(
            bank_data,
            x='period',
            y=['nim_pct', 'casa_pct'],
            markers=True,
            title=f"{selected_bank} - Profitability & Funding",
            labels={'nim_pct': 'NIM%', 'casa_pct': 'CASA%'}
        )
        st.plotly_chart(fig_prof, use_container_width=True)
        
        # Data table
        st.subheader("Quarterly Data")
        display_cols = ['period', 'gnpa_pct', 'nnpa_pct', 'nim_pct', 'casa_pct']
        st.dataframe(bank_data[display_cols].sort_values('period', ascending=False), 
                    use_container_width=True)
    else:
        st.warning(f"No data found for {selected_bank}")

# ===== PAGE 3: PEER COMPARE =====
elif page == "🏆 Peer Compare":
    st.title("🏆 Peer Comparison")
    
    # Metric selector
    metric = st.radio("Select Metric:", ["GNPA% (Lower is Better)", "NIM% (Higher is Better)", "CASA% (Higher is Better)"])
    
    latest = df.loc[df.groupby('bank')['period'].idxmax()]
    
    if metric == "GNPA% (Lower is Better)":
        col_name = 'gnpa_pct'
        ascending = True
        title = "Lowest GNPA% - Best Asset Quality"
    elif metric == "NIM% (Higher is Better)":
        col_name = 'nim_pct'
        ascending = False
        title = "Highest NIM% - Best Profitability"
    else:
        col_name = 'casa_pct'
        ascending = False
        title = "Highest CASA% - Best Funding"
    
    sorted_data = latest.sort_values(col_name, ascending=ascending)
    
    # Bar chart
    fig_bar = px.bar(
        sorted_data,
        x='bank',
        y=col_name,
        title=title,
        color=col_name,
        color_continuous_scale='RdYlGn_r' if metric == "GNPA% (Lower is Better)" else 'RdYlGn',
        labels={col_name: metric.split('(')[0].strip()}
    )
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Quadrant analysis
    st.subheader("📍 Quadrant View: CASA vs GNPA")
    st.markdown("**Best position: Top-Right (High CASA + Low GNPA)**")
    
    fig_scatter = px.scatter(
        latest,
        x='casa_pct',
        y='gnpa_pct',
        hover_name='bank',
        size_max=30,
        title="CASA% vs GNPA%",
        labels={'casa_pct': 'CASA%', 'gnpa_pct': 'GNPA%'},
        text='bank'
    )
    
    fig_scatter.update_traces(textposition='top center')
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Quadrant breakdown
    casa_median = latest['casa_pct'].median()
    gnpa_median = latest['gnpa_pct'].median()
    
    st.subheader("Quadrant Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        best = latest[(latest['casa_pct'] > casa_median) & (latest['gnpa_pct'] < gnpa_median)]['bank'].tolist()
        caution = latest[(latest['casa_pct'] > casa_median) & (latest['gnpa_pct'] >= gnpa_median)]['bank'].tolist()
        
        st.success(f"✅ **BEST** (High CASA + Low GNPA): {', '.join(best) if best else 'None'}")
        st.warning(f"⚠️ **CAUTION** (High CASA + High GNPA): {', '.join(caution) if caution else 'None'}")
    
    with col2:
        watch = latest[(latest['casa_pct'] <= casa_median) & (latest['gnpa_pct'] < gnpa_median)]['bank'].tolist()
        worst = latest[(latest['casa_pct'] <= casa_median) & (latest['gnpa_pct'] >= gnpa_median)]['bank'].tolist()
        
        st.info(f"🔍 **WATCH** (Low CASA + Low GNPA): {', '.join(watch) if watch else 'None'}")
        st.error(f"❌ **WORST** (Low CASA + High GNPA): {', '.join(worst) if worst else 'None'}")
    
    # Full rankings table
    st.subheader("Full Rankings Table")
    rankings = latest.sort_values('gnpa_pct')[['bank', 'gnpa_pct', 'nim_pct', 'casa_pct']]
    st.dataframe(rankings, use_container_width=True)

# ===== PAGE 4: DATA & SOURCES =====
elif page == "📚 Data & Sources":
    st.title("📚 Data & Sources")
    
    # Raw data
    st.subheader("Raw Data")
    st.dataframe(df, use_container_width=True)
    
    # Download
    st.subheader("📥 Download")
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"bank_metrics_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )
    
    # Source attribution
    st.subheader("📖 Source Attribution")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        selected_bank = st.selectbox("Select Bank:", sorted(df['bank'].unique()), key='bank_select')
    
    with col2:
        selected_period = st.selectbox("Select Period:", sorted(df['period'].unique(), reverse=True), key='period_select')
    
    record = df[(df['bank'] == selected_bank) & (df['period'] == selected_period)]
    
    if len(record) > 0:
        r = record.iloc[0]
        
        st.write(f"**Bank:** {selected_bank}")
        st.write(f"**Period:** {selected_period}")
        st.write(f"**Metrics:**")
        st.write(f"  - GNPA%: {r['gnpa_pct']:.2f}%")
        st.write(f"  - NNPA%: {r['nnpa_pct']:.2f}%")
        st.write(f"  - NIM%: {r['nim_pct']:.2f}%")
        st.write(f"  - CASA%: {r['casa_pct']:.2f}%")
        
        st.write(f"**Source Date:** {r['source_doc_date']}")
        
        if pd.notna(r['source_url']):
            st.write(f"**Source URL:** [Link]({r['source_url']})")
        
        if pd.notna(r['notes']):
            st.write(f"**Notes:** {r['notes']}")
    else:
        st.warning(f"No data for {selected_bank} - {selected_period}")

# ===== FOOTER =====
st.markdown("---")
st.markdown("""
    **The Mountain Path - World of Finance** | Prof. V. Ravichandran  
    NPA Analysis Dashboard | January 2026
""")
