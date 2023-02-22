# %[flags][width][.precision]specifier

# chiều rộng bằng 8
# căn phải (mặc định)
print("Hi!__%8s__" % "LyLy")
#>> Hi!__    LyLy__

# căn trái
print("Hi!__%-8s__" % "LyLy")
#>> Hi!__LyLy    __

# đệm 0 (chỉ có tác dụng với số)
# căn trái
print("__%08d__" % 12)
#>> __00000012__

# đệm 0, width = 8 (tính cả dấu chấm), làm tròn 3 chứ số sau đấu chấm
# căn trái
print("__%08.3f__" % 12.34567)
#>> __0012.346__

# đệm 0, width = 8 (tính cả dấu chấm), làm tròn 3 chứ số sau đấu chấm
# căn trái
print("__%8.3f__" % 12.34567)
#>> __0012.346__