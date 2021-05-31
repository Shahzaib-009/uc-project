import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Inches to Feet")
     a = st.number_input("Enter length in inches:")
     b = ( a / 12 )  
     st.text("Length in feet is:")
     st.write(b)
     c = st.number_input("Enter length in feet:")
     d = ( c * 12 )  
     st.text("Length in inches is:")
     st.write(d)
    