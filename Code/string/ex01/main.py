import re

s = """the abc is abc is abc bcd abcbcd
abc is bcd is abc"""

l = re.findall(r"\babc.*abc\b", s)
print(l)
#>> ['abc is abc is abc', 'abc is bcd is abc']

l = re.findall(r"\Aabc.*abc\b", s)
print(l)
#>> []

l = re.findall(r"^abc.*abc\b", s)
print(l)
#>> []


# l = re.findall(r"^The.*name\b", s)
# print(l)

# l = re.findall(r"\ATh.*name\b", s)
# print(l)

# l = re.findall(r"\bTh.*ame\b", s)
# print(l)