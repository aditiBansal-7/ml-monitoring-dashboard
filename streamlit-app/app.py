import pandas as pd
import streamlit as st
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset

# Set Streamlit page config
st.set_page_config(
    page_title="ML Monitoring Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define dataset path
DATA_PATH = "homes.csv"

# Load dataset with caching
@st.cache_data
def load_data():
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if error occurs

df = load_data()

# Sidebar options
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📊 Data Preview", "📉 Data Drift", "✅ Data Quality"])

# Home Page
if page == "🏠 Home":
    st.title("🏡 ML Monitoring Dashboard")
    st.markdown("This dashboard allows monitoring of housing data using Evidently and Streamlit.")

    # Display dataset info
    st.subheader("📌 Dataset Overview")
    st.write(f"✅ **Number of Rows:** {df.shape[0]}")
    st.write(f"✅ **Number of Columns:** {df.shape[1]}")
    st.write("### 🔍 Sample Data")
    st.dataframe(df.head())

# Data Preview Page
elif page == "📊 Data Preview":
    st.title("📊 Data Exploration")
    st.write("Use this section to explore the dataset.")

    # Show dataset statistics
    st.subheader("📌 Dataset Summary")
    st.write(df.describe())

    # Column selection
    column = st.selectbox("📌 Select a Column to View Details", df.columns)
    st.write("**Unique Values**:", df[column].nunique())
    st.write("**Missing Values**:", df[column].isna().sum())

    # Histogram
    st.subheader(f"📈 Histogram of {column}")
    st.bar_chart(df[column].value_counts())

# Data Drift Analysis
elif page == "📉 Data Drift":
    st.title("📉 Data Drift Report")

    # Generate Evidently Data Drift Report
    drift_report = Report(metrics=[DataDriftPreset()])
    drift_report.run(reference_data=df.sample(frac=0.5, random_state=42), current_data=df)
    
    # Display report
    st.subheader("🔍 Data Drift Report")
    st.write("This report compares the reference dataset with the current dataset to detect drift.")
    st.components.v1.html(drift_report.get_html(), height=800, scrolling=True)

# Data Quality Analysis
elif page == "✅ Data Quality":
    st.title("✅ Data Quality Report")

    # Generate Evidently Data Quality Report
    quality_report = Report(metrics=[DataQualityPreset()])
    quality_report.run(reference_data=df, current_data=df)

    # Display report
    st.subheader("🔍 Data Quality Report")
    st.write("This report checks for missing values, duplicates, and other quality issues.")
    st.components.v1.html(quality_report.get_html(), height=800, scrolling=True)

