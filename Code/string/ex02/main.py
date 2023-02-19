import re

s = """the abc is bcd"""


l = re.findall(r"\Ath.*", s)
print(l)
#>> ['the abc is bcd']

l = re.findall(r"^th.*", s)
print(l)
#>> ['the abc is bcd']

# lỗi khoảng trắng
l = re.findall(r"^ th.*", s)
print(l)
#>> []