""""

"""
import pandas as pd
import numpy as np

def read_data():
    df = pd.read_csv("Projects\\app_ventas\\data.csv")
    return df

def format_string(string):
    string = string.lower()
    string = string.replace(" ", "")
    return string

def search(material, df):
    material = format_string(material)
    return df[df["material"].apply(format_string) == material]


    
