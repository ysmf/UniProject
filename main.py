import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Top TF-IDF Words",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Top TF-IDF Words")

# ดึง DataFrame จากไฟล์ CSV
tfidf_df = pd.read_csv('tfidf_results.csv')

data = {
    "Word": tfidf_df["word"],
    "TF-IDF": tfidf_df["tfidf"]
}

# สร้าง DataFrame
df = pd.DataFrame(data)

# หาคำที่มีค่า TF-IDF สูงสุด
max_tfidf_word = df.loc[df['TF-IDF'].idxmax()]

# สร้างคอลัมน์เพื่อแบ่งพื้นที่จอให้สมดุล
col1, col2 = st.columns([1, 1])

# แสดงตารางข้อมูลทางฝั่งซ้ายในส่วนขยายได้
with col1:
    with st.expander("ดูตารางข้อมูล TF-IDF"):
        st.write("### ข้อมูล TF-IDF")
        st.dataframe(df)

# แสดงคำฮิตประจำสัปดาห์ทางฝั่งขวา พร้อมเพิ่มขนาดตัวอักษร
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
#สร้าง sidebar
st.sidebar.markdown("**Choose a Trend:**")
