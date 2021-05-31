import numpy as np
import streamlit as st
import math
import csv
from PIL import Image
import pandas as pd


def app():
     st.title("Celsius to Fahrenheit ")
     a = st.number_input("Enter temprature in celsius:")
     b = ( a * 9/5 ) + 32 
     st.text("Temprature in fahrenheit is:")
     st.write(b)
     c = st.number_input("Enter temprature in fahrenheit:")
     d = ( c -32 ) * 5/9 
     st.text("Temprature in Celsius is:")
     st.write(d)
    