a = int(input())
b = int(input())
counter = 0

for i in range (a, b + 1):
    cube = i ** 3
    dig1 = cube // 1000
    dig2 = (cube // 100) % 10
    dig3 = (cube // 10) % 10
    dig4 = cube % 10
    if dig4 == 4 or dig4 == 9:
        counter += 1
print (counter)