import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Grams to Kilograms")
     a = st.number_input("Enter weight in grams:")
     b = ( a / 1000 )  
     st.text("Weight in kilograms is:")
     st.write(b)
     c = st.number_input("Enter weight in kilograms:")
     d = ( c * 1000 ) 
     st.text("Weight in grams is:")
     st.write(d)
    