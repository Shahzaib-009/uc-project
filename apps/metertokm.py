import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Meters to kilometers")
     a = st.number_input("Enter length in meters:")
     b = ( a / 1000)  
     st.text("Length in kilometer is:")
     st.write(b)
     c = st.number_input("Enter length in kilometers:")
     d = ( c * 1000) 
     st.text("Length in meters is:")
     st.write(d)
    