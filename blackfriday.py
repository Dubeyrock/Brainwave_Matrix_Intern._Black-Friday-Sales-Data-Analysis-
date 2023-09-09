


import numpy as np
import pandas as pd
import streamlit as st
#from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


# subheader 
st.header("Black Friday Sales Data Analysis")

# Web App Title
st.markdown('''
# **The Data Analysis App**

This is the ** Black Friday Sales Data Analysis EDA App** created in Streamlit using the **pandas-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by [Shivam Dubey](https://medium.com/@shivvam2002) (Linkdin [Computer Science Student](https://www.linkedin.com/in/shivam-dubey-371a591a8/))

---
''')

st.write("Black Friday is a shopping holiday that takes place on the day after Thanksgiving. It is known for its deep discounts and special deals on a wide range of products, including electronics, home goods, clothing, and more. Many retailers offer special doorbuster deals and extended hours on Black Friday, and it is traditionally one of the busiest shopping days of the year.")

# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](BlackFriday (1).csv)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache_data
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e']
            )
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)