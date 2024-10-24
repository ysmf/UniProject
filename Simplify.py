from pythainlp.tokenize import Tokenizer

# เปิดไฟล์ custom dictionary และอ่านคำในไฟล์
with open("words_th.txt", encoding="utf-8") as f:
    custom_words = f.read().splitlines()

# สร้างตัว Tokenizer ด้วย custom dictionary
tokenizer = Tokenizer(custom_words)

textN = "He reads many books."
tokensN = tokenizer.word_tokenize(textN)
b_join = ''.join(tokensN)
a_join = [b_join]
print(a_join)

