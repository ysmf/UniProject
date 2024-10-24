from Simplify import cleaned_data  # ใช้ cleaned_data ที่ผ่านการตัดคำแล้ว
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os

# คำนวณ TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_data)

feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray().flatten()

# ตรวจสอบความยาวของ feature_names และ tfidf_scores
print("Length of feature_names:", len(feature_names))
print("Length of tfidf_scores:", len(tfidf_scores))

# สร้าง DataFrame
if len(feature_names) == len(tfidf_scores):
    tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf': tfidf_scores})
    tfidf_df = tfidf_df.sort_values(by='tfidf', ascending=False)
    
    # เขียน DataFrame ลงไฟล์ CSV
    tfidf_df.to_csv('tfidf_results.csv', index=False)  # เขียนทับไฟล์หากมีอยู่แล้ว
    print("File 'tfidf_results.csv' created/updated successfully.")
else:
    print("Error: Length mismatch between feature_names and tfidf_scores")
