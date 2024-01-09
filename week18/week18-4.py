# Chapter 2
#a = int(input())
a = int( '12345677' )
print( a + 999)
# bool() False True
# int() 0 1 2 100 1999 -33
# float() 3.1415 2.7182 ..
# str() '單引號' "雙引號"
ans = type('12345')
print(ans)

# 字串
a = 'hello'
b = 'world'
print( a+b )
print( a*3 )
print( a[0], a[-1] )

a = list(map(int, '10 20 30'.split() ))
print(a)
a = ['hello', 'word', 'very', 'good']
print( a[0]+a[1] )
print( '###'.join(a) )