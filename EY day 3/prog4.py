import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Page content
st.title("Student Performance Dashboard")
st.write("This dashboard shows sample data about student marks.")

# Create sample data
# Suppose there are marks of 5 students over 3 tests
data = {
    "Test 1": [65, 70, 80, 75, 90],
    "Test 2": [68, 72, 78, 80, 92],
    "Test 3": [70, 75, 82, 85, 95]
}

# Convert data into a DataFrame
df = pd.DataFrame(data, index=["Student A", "Student B", "Student C", "Student D", "Student E"])

# Display the DataFrame
st.subheader("Marks Data")
st.dataframe(df)

# Display a line chart
st.subheader("Performance Trend (Line Chart)")
st.line_chart(df.T)