a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(a,b,c, sep='\n')
else: 
    d = int()
    d = (a + b + c)
    print(max(a,b,c)) # max 
    print(d - min(a,b,c) - max(a,b,c)) # mid
    print(min(a,b,c)) # min