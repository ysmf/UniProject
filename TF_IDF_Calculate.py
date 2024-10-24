from Simplify import cleaned_data  # เปลี่ยนจาก a_join เป็น cleaned_data
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# คำนวณค่า TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_data)
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray().flatten()

# สร้าง DataFrame สำหรับเก็บคำและค่า TF-IDF
tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf': tfidf_scores})
tfidf_df = tfidf_df.sort_values(by='tfidf', ascending=False)

# แสดงผลลัพธ์
print(tfidf_df)
