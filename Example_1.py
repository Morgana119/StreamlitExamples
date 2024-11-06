import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Police1.csv")
