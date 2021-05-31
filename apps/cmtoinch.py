import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("centimeters to Inches")
     a = st.number_input("Enter length in centimeter:")
     b = ( a / 2.54 )  
     st.text("Length in inches is:")
     st.write(b)
     c = st.number_input("Enter length in inches:")
     d = ( c * 2.54 ) 
     st.text("Length in centimeters is:")
     st.write(d)
    