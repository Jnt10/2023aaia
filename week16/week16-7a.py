# SOIT108_ADVANCE_002B
a = list(map(int, input().split() ))
a.sort()
# a[0] + a[1]*10 +a[2]*100
ans =  a[0] + a[1]*10 +a[2]*100 + 1
print( ans , end='' )