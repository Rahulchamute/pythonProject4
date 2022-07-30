import re

# text = """ 12345 12345
#            5432109
# """
#
# res = re.findall("[0-9]",text)
# print(res)

# text="""12345 12345
#         54321109
# """
# res=re.findall("[0-9]{5}",text)
# print(res)

# text = """ QWDFR5665P
#             QDGGR5555P
# """
# res=re.findall("[A-Z]{5}[0-9]{4}[A-Z]",text)
# print(res)

# text = """ QWDFR5665P
#             QDGGR5555P
# """
# res=re.findall("[A-Z]{5}\d{4}[A-Z]",text)
# print(res)

# text = """ QWDFR5665P
#             QDGGR5555P
#
#             1234 5678 9090
# """
# res=re.findall("[A-Z]{5}\d{4}[A-Z]",text)
# print(res)
# res=re.findall("\d{4}[ ]\d{4}[ ]\d{4}",text)
# print(res)

# text = """ QWDFR5665P
#             QDGGR5555P
#
#             1234 5678 9090
# """
#
# res = re.findall("\D", text)
# print(res)

# text = """ QWDFR5665P
#             QDGGR5555P
#
#             1234 5678 9090
# """
# res=re.findall("\d{4}\s\d{4}\s\d{4}",text)
# print(res)

# text = """Data science is an interdisciplinary field that uses scientific methods,
# processes, algorithms and systems to extract knowledge and insights from noisy,
# structured and unstructured data, and apply knowledge and actionable insights
# from data across a broad range of application domains.
# QWDFR5665P
# QDGGR5555P
#
# 1234 5678 9090
# """
#
# res = re.findall("\w{5}", text)
# print(res)


# text = """Bank IFSC Code is :
#           HDFC0009873
#           HDFC000987356789
#
#           9888989878
#           988898987856
#           ASDFG7436Q
#           QSDFG4568POIUY
# """
#
# Bank_id = re.findall(r"\b[A-Z]{4}\d{7}\b", text)
# print(Bank_id)
# Bank_id1=re.findall(r"\b[A-Z]{4}\d{12}\b",text)
# print(Bank_id1)

# text = """
# PAN CARDs
# QWERT5675T
# DFGSR2342Y
# WRERD2342E
# ERTWE2345C
# 9988778767
# 988877665544
# 1234 5678 9090
# """
# pan=re.search(r"\b[A-Z]{5}\d{4}[A-Z]\b",text)
# pan
# print(pan.group())

# text = """DFGSR2342Y
# QWERT5675T
# WRERD2342E
# ERTWE2345C
# 9988778767
# 988877665544
# 1234 5678 9090
# """
#
# pan = re.match(r"[A-Z]{5}\d{4}[A-Z]", text)
# if pan:
#     print(f"Match found = {pan.group()}")
#
# else:
#     print("No Match found")

# text = """Data Science and Machine learning"""
# str_res = text.replace("Data Science","Python")
# print(str_res)

# text = """Data Science      and      Machine @@@@ learning"""
# str_res=re.sub("@","",text)
# print(str_res)

# text = """Data Science      and   !@#$%^   Machine @@@@ learning 12345"""
# str_res=re.sub("\s+"," ",text)
# print(str_res)

# text = """Python Pyttthon Pythoon """
# res=re.findall("Pyt+ho+n",text)
# print(res)

# text = "python pyhon pyhn"
# res = re.findall("pyt*hon",text)
# print(res)
# res = re.findall("pyt*ho*n",text)
# print(res)

# data = """data science"""
# res = re.findall("d.ta",data)
# print(res)

# data = "python data science pyhon pytthhhhon"
# res=re.findall("pyt?hon",data)
# print(res)

# data = "python data science pyhon pytthhhhon"
# res = re.findall("^p",data)
# print(res)

# data="Python"
# res=re.findall("n$",data)
# print(res)
