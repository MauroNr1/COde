import streamlit as st
import pandas as pd
import numpy as np
from openai import OpenAI
import time

##GLOBALS

st.title(":sunglasses: Dataverwerking")
st.markdown("Upload een **.CSV bestand** van de enquête-antwoorden:")

csv_file = st.file_uploader("CSV bestand uploaden",type="csv",label_visibility="collapsed")

if csv_file:
    file = pd.read_csv(csv_file)