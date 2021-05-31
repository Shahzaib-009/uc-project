import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app(): 
     st.title("Nanometers to Micrometers")
     a = st.number_input("Enter length in nanometer:")
     b = ( a / 1000 )  
     st.text("Length in micrometers is:")
     st.write(b)
     c = st.number_input("Enter length in micrometers:")
     d = ( c * 1000 ) 
     st.text("Length in nanometers is:")
     st.write(d)
    