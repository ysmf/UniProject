import re
from pythainlp.tokenize import Tokenizer

# ฟังก์ชันทำความสะอาดข้อมูล
def clean_text(text):
    # ลบตัวอักษรพิเศษที่ไม่ต้องการ
    text = re.sub(r'[^ก-๙a-zA-Z0-9\s#]', '', text)
    return text

# ฟังก์ชันตัดคำ
def tokenize_posts(posts):
    # เปิดไฟล์ custom dictionary และอ่านคำในไฟล์
    with open("words_th.txt", encoding="utf-8") as f:
        custom_words = f.read().splitlines()
    
    # สร้างตัว Tokenizer ด้วย custom dictionary
    tokenizer = Tokenizer(custom_words)
    
    tokenized_results = []
    for post in posts:
        cleaned_post = clean_text(post)
        tokens = tokenizer.word_tokenize(cleaned_post)
        b_join = ''.join(tokens)
        tokenized_results.append(b_join)
    
    return tokenized_results

# ชุดข้อมูลโพสต์
posts = [
    "ข่าวล่าสุด: มีการเผยแพร่ภาพใหม่ของมือปืน ตัวจริงเสียงจริง ที่แสดงวินาทีที่มือปืนโทมัส แมทธิว ครูกส์ เปิดฉากยิงใส่การชุมนุมของทรัมป์ที่บัตเลอร์เคาน์ตี้ รัฐเพนซิลเวเนีย และวินาทีต่อมาเขาก็ถูกมือปืนหน่วยสืบราชการลับสังหาร#Us #Trump #ทรัมป์ #Us #สหรัฐอเมริกา #Pennsylvania",
    "สังเกตทุกครั้งที่เกิดดราม่า มันไม่ใช่เพราะตัว #คัลแลนพี่จอง เลยสักครั้ง เเต่มันเกิดจากคนอื่นทั้งนั้นจริงๆ ทั้งไก่ทอดหาดใหญ่ ทั้งไกด์ชุมพร เกาะปันหยี เห็นเขาใจดีต้องเกรงใจ ไม่ใช่เอาเปรียบ คนพวกนั้นมันต้องโดนสาปถูกเเล้ว",
    "นาทีชีวิต ชายคนนี้เป็นแพทย์ เล่านาทีช่วยชีวิตชายผู้บริสุทธิ์ที่ถูกยิงที่ศีรษะในการชุมนุมของโดนัลด์ ทรัมป์ #โดนัลด์ทรัมป์ #ทรัมป์ #Trump",
    "เชื่อปะการถูกรอบยิงประธานาธิบดีและอดีตประธานาธิบดีสหรัฐฯ ไม่ได้เกิดขึ้นครั้งแรก มันมีหลายครั้งและหลายเหตุการณ์ แต่ทรัมป์ถือว่าโชคดีมากๆที่ยังโดนแค่เพียงหู แต่ที่หน้าแปลกใจว่าระบบการป้องกันบุคคล ถึงดูปล่อยปะละเลยขนาดนี้ #ทรัมป์ #Trump"
]

# เรียกใช้ฟังก์ชัน
a_join = tokenize_posts(posts)
