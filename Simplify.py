import re
import pandas as pd

# ฟังก์ชันสำหรับทำความสะอาดข้อความ
def clean_text(text):
    # ลบช่องว่างซ้ำซ้อน
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ข้อมูลตัวอย่าง (เปลี่ยนเป็นข้อมูลจริงของคุณ)
raw_data = [
    "ข่าวล่าสุด: มีการเผยแพร่ภาพใหม่ของมือปืน ตัวจริงเสียงจริง ที่แสดงวินาทีที่มือปืนโทมัส แมทธิว ครูกส์ เปิดฉากยิงใส่การชุมนุมของทรัมป์ที่บัตเลอร์เคาน์ตี้ รัฐเพนซิลเวเนีย และวินาทีต่อมาเขาก็ถูกมือปืนหน่วยสืบราชการลับสังหาร#Us #Trump #ทรัมป์ #Us #สหรัฐอเมริกา #Pennsylvania",
    "สังเกตทุกครั้งที่เกิดดราม่า มันไม่ใช่เพราะตัว #คัลแลนพี่จอง เลยสักครั้ง เเต่มันเกิดจากคนอื่นทั้งนั้นจริงๆ ทั้งไก่ทอดหาดใหญ่ ทั้งไกด์ชุมพร เกาะปันหยี เห็นเขาใจดีต้องเกรงใจ ไม่ใช่เอาเปรียบ คนพวกนั้นมันต้องโดนสาปถูกเเล้ว",
    "นาทีชีวิต ชายคนนี้เป็นแพทย์ เล่านาทีช่วยชีวิตชายผู้บริสุทธิ์ที่ถูกยิงที่ศีรษะในการชุมนุมของโดนัลด์ ทรัมป์ #โดนัลด์ทรัมป์ #ทรัมป์ #Trump",
    "เชื่อปะการถูกรอบยิงประธานาธิบดีและอดีตประธานาธิบดีสหรัฐฯ ไม่ได้เกิดขึ้นครั้งแรก มันมีหลายครั้งและหลายเหตุการณ์ แต่ทรัมป์ถือว่าโชคดีมากๆที่ยังโดนแค่เพียงหู แต่ที่หน้าแปลกใจว่าระบบการป้องกันบุคคล ถึงดูปล่อยปะละเลยขนาดนี้ #ทรัมป์ #Trump"
]

# ทำความสะอาดข้อมูล
cleaned_data = [clean_text(item) for item in raw_data]

# สร้าง DataFrame
df_cleaned = pd.DataFrame(cleaned_data, columns=['cleaned_text'])

# บันทึก DataFrame ลงไฟล์ CSV
df_cleaned.to_csv('cleaned_data.csv', index=False)
