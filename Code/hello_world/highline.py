import re

txt = "the abc123 in the bcd456 better than the abc123"


x = re.findall("a[a-z]*", txt)
print(x)
#>>['abc', 'an', 'abc']

x = re.search("a[a-z]*", txt)
print(x)
#>><re.Match object; span=(4, 7), match='abc'>
print(x.start())
#>>4

x = re.findall("\d+", txt)
print(x)
#>>['123', '456', '123']

x = re.findall("^the.*abc", txt)
print(x)
#>>['the abc123 in the bcd456 better than the abc']

