import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# โหลดข้อมูลที่ทำความสะอาดแล้ว
cleaned_df = pd.read_csv('cleaned_data.csv')

# สร้าง TfidfVectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(cleaned_df['cleaned_text'])

# ดึงฟีเจอร์และคะแนน TF-IDF
feature_names = vectorizer.get_feature_names_out()
tfidf_scores = tfidf_matrix.toarray()

# ตรวจสอบความยาว
if len(feature_names) != len(tfidf_scores[0]):
    raise ValueError("Length mismatch between feature_names and tfidf_scores")

# สร้าง DataFrame สำหรับ TF-IDF
tfidf_df = pd.DataFrame({'word': feature_names, 'tfidf': tfidf_scores[0]})

# บันทึกผลลัพธ์ลงไฟล์ CSV
tfidf_df.to_csv('tfidf_results.csv', index=False)
