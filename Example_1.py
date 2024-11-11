import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Policev1.csv")
df

st.markdown('The data shown below belongs to incident reports in the city of San Francisco, from the reat 2018 to 2020.')

mapa = pd.DataFrame()
mapa ['Date'] = df['Incident Date']
mapa ['Day'] = df['Incident Day of week']
mapa ['Police District'] = df['Police District']
mapa ['Date'] = df['Incident Date']
mapa ['Neighborhood'] = df['Analysis Neighborhood']
mapa ['Incident Category'] = df['Incident Category']
mapa ['Incident Subcategory'] = df['Incident Subcategory']
mapa ['Resolution'] = df['Resolution']
mapa ['lat'] = df['Latitude']
mapa ['lon'] = df['Longitude']
mapa = mapa.dropna()

