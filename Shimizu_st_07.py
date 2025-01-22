import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Relation sales and ad expense')

df = pd.read_csv('ad_expense_sales.csv')

with st.sidebar:
    st.subheader('Selection conditions')
    # st.subheader('Please select product category')
    prod_category = st.multiselect('Please select product category',
                            df['prod_category'].unique(),
                            default='air cleaner',
                            key='c1')
    # st.subheader('Please select media')
    media = st.selectbox('Please select media',
                            df['media'].unique(),
                            key='m1')
    
    st.subheader('Coloring')
    color = st.selectbox('Please select color',
                            ['sex', 'age', 'season'],
                            key='c2')
df = df[df['prod_category'].isin(prod_category)]
df = df[df['media']==media]
# df = df[df['color']==color]

# st.dataframe(df, width=800, height=420)
fig = px.scatter(df,
                 x='ad_expense',
                 y='sales',
                 color=color,
                 labels = {'ad_expense': 'Ad expense (10000 yen)',
                           'sales': 'Sales (10000 yen)'},
                 range_x=[0, df['ad_expense'].max()*1.1],
                 range_y=[0, df['sales'].max()*1.1],
                 trendline='ols',
                 )
st.plotly_chart(fig, use_container_width=True)

