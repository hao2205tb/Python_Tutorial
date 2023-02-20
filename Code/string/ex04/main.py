# Xoá các ký tự khoảng trắng, o và l trong chuỗi
org_str = "  hello world  "
new_str = org_str.replace(" ", "")
new_str = new_str.replace("o", "")
new_str = new_str.replace("l", "")
print('[' + new_str + ']')
#>> [hewrd]
