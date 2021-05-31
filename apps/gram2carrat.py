import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Grams to Carats")
     a = st.number_input("Enter weight in grams:")
     b = ( a * 5 )  
     st.text("Weight in carats is:")
     st.write(b)
     c = st.number_input("Enter weight in carats:")
     d = ( c / 5) 
     st.text("Weight in grams is:")
     st.write(d)
    