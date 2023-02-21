s1 = 'abcde'
s2 = 'cde'
s3 = 'abcdef'

print( set(s1) ^ set(s2) )
#>> {'b', 'a'}

print( set(s1) ^ set(s3) )
#>> {'f'}

print(type(set(s1) ^ set(s3)))
#>> <class 'set'>
