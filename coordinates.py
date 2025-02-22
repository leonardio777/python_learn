a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

# both coordinates even or both coordinates uneven
if ((a1 % 2 != 0 and a2 % 2 != 0) and (b1 % 2 != 0 and b2 % 2 != 0)) or ((a1 % 2 == 0 and a2 % 2 == 0) and (b1 % 2 == 0 and b2 % 2 == 0)):
    print ('YES')
# one coordinate fully even and another one fully uneven
elif ((a1 % 2 == 0 and a2 % 2 == 0) and (b1 % 2 != 0 and b2 % 2 != 0)) or ((a1 % 2 != 0 and a2 % 2 != 0) and (b1 % 2 == 0 and b2 % 2 == 0)):
    print ('YES')
# a1 even, a2 uneven, b1 even, b2 uneven
elif ((a1 % 2 == 0 and a2 % 2 != 0)) and ((b1 % 2 == 0 and b2 % 2 != 0)):
    print ('YES')
# a1 uneven, a2 even, b1 uneven, b2 even
elif ((a1 % 2 != 0 and a2 % 2 == 0)) and ((b1 % 2 != 0 and b2 % 2 == 0)):
    print ('YES')
# a1 even, a2 uneven, b1 uneven, b2 even
elif ((a1 % 2 == 0 and a2 % 2 != 0)) and ((b1 % 2 != 0 and b2 % 2 == 0)):
    print ('YES')
# a1 uneven, a2 even, b1 even, b2 uneven
elif ((a1 % 2 != 0 and a2 % 2 == 0)) and ((b1 % 2 == 0 and b2 % 2 != 0)):
    print ('YES')
else:
    print ('NO')