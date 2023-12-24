import pandas as pd
import streamlit as st
import plotly.express as px
import base64
from streamlit_extras.dataframe_explorer import dataframe_explorer


st.set_page_config(page_title='Sprint 4 Project', page_icon='https://img.icons8.com/?size=512&id=24733&format=png')

#https://raw.githubusercontent.com/hotmetalbabe/sprint4/blob/5c36d5b03233bea442c5ea73894af6f49659533c/real_madrid.csv
df = pd.read_csv('real_madrid.csv')

st.title('Real Madrid Player Wages')

st.markdown("""
This app drills down into 5 seasons of Real Madrid player wage stats data
* **Python libraries:** base64, pandas, streamlit, plotly.express
* **Data source:** [FBref.com](https://fbref.com/en/squads/53a2f082/2022-2023/wages/Real-Madrid-Wage-Details)
""")


# add_logo('https://www.vecteezy.com/vector-art/10994307-real-madrid-logo-symbol-black-and-white-design-spain-football-vector-european-countries-football-teams-illustration', height=300)

# Filtering Data

show_data = st.checkbox('Show me the money 💸')
if show_data:
    st.header('Wage Stats (£)')
    filtered_df = dataframe_explorer(df, case=False)
    st.dataframe(filtered_df, use_container_width=True)
    st.write('Data Dimensions: ' + str(filtered_df.shape[0]) + ' rows and ' + str(filtered_df.shape[1]) + ' columns.')


# Option to download the CSV file
def filedownload(df):
  csv = df.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()
  href = f'<a href="data:file/csv;base64,{b64}" download="real_madrid.csv">Download CSV File</a>'
  return href

st.markdown(filedownload(df), unsafe_allow_html=True)
                                 
# Charts

if st.button('Country Histogram'):
    st.header('Player Nationality by Age Group')
    country_hist = px.histogram(df, x='Age', marginal = 'violin',
             range_x=(14,40), animation_frame='Season',nbins=5, range_y=(0,15), width=1500, color='Nation', height=1000)                                       
    st.plotly_chart(country_hist,use_container_width=True)

if st.button('Wages Histogram'):
    st.header('Total Annual Wages by Position (£)')
    wages_hist = px.histogram(df, x='Season', y='Annual Wages', color='Pos', hover_data='Annual Wages', barmode='overlay',width=1500,
           animation_frame='Pos', height=1000)                                    
    st.plotly_chart(wages_hist,use_container_width=True)

if st.button('Country Scatterplot'):
    st.header('Annual Wage Distribution by Nation (£)')
    country_scat = px.scatter(df, x='Season', y='Annual Wages',
           hover_data=['Annual Wages', 'Player'], size='Age', render_mode='auto', animation_frame='Nation', width=1500, height=1000, range_y=(0,40000000))                                   
    st.plotly_chart(country_scat,use_container_width=True)
