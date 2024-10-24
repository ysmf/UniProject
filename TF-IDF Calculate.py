from Simplify import a_join
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# ฟังก์ชันคำนวณ TF-IDF
def calculate_tfidf(posts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(posts)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray().flatten()
    
    tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf': tfidf_scores})
    tfidf_df = tfidf_df.sort_values(by='tfidf', ascending=False)
    
    # บันทึกผลลัพธ์เป็นไฟล์ CSV
    tfidf_df.to_csv('tfidf_results.csv', index=False)

# เรียกใช้ฟังก์ชัน
calculate_tfidf(a_join)
