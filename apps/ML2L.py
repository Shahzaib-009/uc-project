import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Milliliters to Liters")
     a = st.number_input("Enter Volume in milliliters:")
     b = ( a / 1000 )  
     st.text("Volume in Liters is:")
     st.write(b)
     c = st.number_input("Enter Volume in Liters:")
     d = ( c * 1000 ) 
     st.text("Volume in milliliters is:")
     st.write(d)
    