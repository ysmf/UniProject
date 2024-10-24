import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Top TF-IDF Words",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Top TF-IDF Words")

# อ่านไฟล์ CSV ที่บันทึกผลลัพธ์จาก TF-IDF
tfidf_df = pd.read_csv('tfidf_results.csv')

# สร้าง DataFrame
data = {
    "Word": tfidf_df["word"],
    "TF-IDF": tfidf_df["tfidf"]
}
df = pd.DataFrame(data)

# หาคำที่มีค่า TF-IDF สูงสุด
max_tfidf_word = df.loc[df['TF-IDF'].idxmax()]

# แสดงตารางข้อมูลทางฝั่งซ้ายในส่วนขยายได้
col1, col2 = st.columns([1, 1])

with col1:
    with st.expander("ดูตารางข้อมูล TF-IDF"):
        st.write("### ข้อมูล TF-IDF")
        st.dataframe(df)

with col2:
    st.write("### คำที่ฮิตประจำสัปดาห์")
    st.markdown(f"<h2 style='font-size: 32px;'>{max_tfidf_word['Word']}</h2>", unsafe_allow_html=True)
    st.write(f"ด้วยค่า TF-IDF: **{max_tfidf_word['TF-IDF']}**")

# ตั้งค่า 'Word' เป็นดัชนี (index) สำหรับการพล็อตกราฟ
df.set_index('Word', inplace=True)

# แสดงกราฟที่ด้านล่าง
st.write("### กราฟ TF-IDF ของคำ")
st.line_chart(df)

st.sidebar.title("Navigation")
st.sidebar.markdown("**Choose a Trend:**")
