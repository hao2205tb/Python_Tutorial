# Xoá khoảng trắng 2 đầu chuỗi
org_str = "  hello world  "
new_str = org_str.strip()
print('[' + new_str + ']')
#>> [hello world]

# xoá các ký tự khoảng trắng, l và o
org_str = "loool hello world loool"
new_str = org_str.strip(" lo")
print('[' + new_str + ']')
#>> [hello world]