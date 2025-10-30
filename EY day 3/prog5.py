import streamlit as st
import pandas as pd
# page title
st.title("streamlit data display Demo")
# -----1. st. Dataframe()----
st.subheader("1. Explore a dtaset (st. dataframe)")
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [24, 30, 22, 35, 28],
    "score": [85, 90, 78, 88, 92],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}
df = pd.DataFrame(data)
st.dataframe(df)
# -----2 st. table()----
st.subheader("2. Display summary data (st. table)")
summary = df.describe()
st.table(summary)