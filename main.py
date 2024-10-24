import streamlit as st
import pandas as pd

# โหลดผลลัพธ์ TF-IDF
try:
    tfidf_df = pd.read_csv('tfidf_results.csv')
    st.title("TF-IDF Results")
    
    # แสดง DataFrame
    st.write(tfidf_df)

except FileNotFoundError:
    st.error("File 'tfidf_results.csv' not found. Please run TF_IDF_Calculate.py first.")
