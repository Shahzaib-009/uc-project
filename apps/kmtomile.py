import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Kilometers to Miles")
     a = st.number_input("Enter length in km:")
     b = ( a / 1.609 )  
     st.text("Length in miles is:")
     st.write(b)
     c = st.number_input("Enter length in miles:")
     d = ( c * 1.609 ) 
     st.text("Length in km is:")
     st.write(d)
    