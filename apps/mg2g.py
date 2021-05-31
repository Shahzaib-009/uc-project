import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Milligrams to Grams")
     a = st.number_input("Enter weight in milligrams:")
     b = ( a / 1000 )  
     st.text("Weight in grams is:")
     st.write(b)
     c = st.number_input("Enter weight in grams:")
     d = ( c * 1000 ) 
     st.text("Weight in grams is:")
     st.write(d)
    