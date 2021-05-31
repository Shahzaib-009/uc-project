import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("kelvin to Celsius")
     a = st.number_input("Enter temprature in kelvin:")
     b = ( a -273.15 ) 
     st.text("Temprature in Celsius is:")
     st.write(b)
     c = st.number_input("Enter temprature in Celsius:")
     d = ( c + 273.15 )
     st.text("Temprature in Kelvin is:")
     st.write(d)
    