# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 21:48:04 2024

@author: megha
"""

#Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

#To ignore warnings
import warnings
warnings.filterwarnings('ignore')
bankruptcy=pd.read_csv("bankruptcy-prevention.csv")
bankruptcy
