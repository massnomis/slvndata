import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json


#st.set_page_config(layout="wide")
# st.title("Polygon Fees")
# st.text ("https://app.flipsidecrypto.com/velocity/queries/5b112bae-b1e2-446c-b458-1eb31900d06e")



df = pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/6c5fbcd3-9156-4e07-954a-5656cb632748/data/latest')

t_f = False
st.sidebar.write("Choose y-axis scale")
check = st.sidebar.checkbox("Linear/Log")
if check: 
    t_f = True


#-------------------------------------------------------

# st.markdown("""
# ### Polygon Fees and Transactions - Base Table
# """)

st.dataframe(df)

# st.markdown("""
# """)


st.sidebar.header("Choose Columns:")
columns = st.sidebar.multiselect(
    "Select the columns to plot",
    options = df.columns,
    default = df.columns.max()
)

# st.sidebar.header("Choose colors:")
# colors = st.sidebar.multiselect(
#     "Select the colors to plot",
#     options = poly_fees_flipside_df.columns,
#     default = poly_fees_flipside_df.NFT
# )

# chart_type = st.text_input('bar, scatter, line','scatter')


bar = px.bar(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = columns,
    color = "RARITY_AND_NFT",
    # title = "<b>DIY / Choose your own adventure - Polygon Fees</b>",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(bar)

scatter = px.scatter(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = columns,
    color = "RARITY_AND_NFT",
    # title = "<b>DIY / Choose your own adventure - Polygon Fees</b>",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)
st.plotly_chart(scatter)

line = px.line(
    df, #this is the dataframe you are trying to plot
    x = "DAY",
    y = columns,
    
    color = "RARITY_AND_NFT",
    # title = "<b>DIY / Choose your own adventure - Polygon Fees</b>",
    orientation = "v",
    template = "plotly_white",
    width = 1000,
    height = 600,
    log_y = t_f
)

st.plotly_chart(line)
