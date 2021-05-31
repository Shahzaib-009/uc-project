import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Pounds to Ounces")
     a = st.number_input("Enter weight in Pounds:")
     b = ( a * 16 )  
     st.text("Weight in ounces is:")
     st.write(b)
     c = st.number_input("Enter weight in ounces:")
     d = ( c / 16 ) 
     st.text("Weight in pounds is:")
     st.write(d)
    