# pattern: [index/key]:[Align][Sign][Width][Grouping_option][.Precision][#][Type]

# Định dạng kiểu dữ liệu (type) ---------------
# chuỗi, nhị phân, bát phân, thập lục phân, phần trăm
print("{:s}, {:b}, {:o}, {:x}, {:%}".format("string", 31, 31, 31, 0.12))
print("{:s}, {:#b}, {:#o}, {:#x}, {:%}".format("string", 31, 31, 31, 0.12))
#>> string, 11111, 37, 1f, 12.000000%
#>> string, 0b11111, 0o37, 0x1f, 12.000000%

# Định dạng độ rộng tối thiểu (width), căn lề, đệm 0 -----------
# căn trái, căn phải, giữa, đệm 0
print("_{:<8}_ _{:>8}_ _{:^8}_ _{:08}_".format("hello", "hello", "hello", 123.4))
#>> _hello   _ _   hello_ _ hello  _ _000123.4_

# Định dạng dấu(sign) (không có ý nghĩa trong python) -------------
print("{:-} {:-} {} {:+}".format(123.4, -123.4, -123.4, -123.4))
#>> 123.4 -123.4 -123.4 -123.4

# Định dạng dấu phân tách cụm 3 số cho dễ nhìn (group_option) --------------
# định dạng với số nguyên
d = 12345678
print("{:,}  {:_}  {:014,}".format(d, d, d))
#>> 12,345,678  12_345_678  00,012,345,678

# định dạng với số thập phân
f = 1234.5678
print("{:,}  {:014,}  {:014,.5f}".format(f, f, f))
#>> 1,234.5678  0,001,234.5678  0,001,234.56780

# định dạng .precision ----------------------------------------------------
f = 1234.5678
print("{:.2f}  {:014.5f}  {:014,.5f} ".format(f, f, f))
#>> 1234.57  00001234.56780  0,001,234.56780

print("{:.2}  {:014.5}  {:014,.5} ".format(f, f, f))
#>> 1.2e+03  000000001234.6  0,000,001,234.6