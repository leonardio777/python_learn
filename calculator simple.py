a = int(input())
b = int(input())
c = input()

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/" and b == 0:
    print("Division by 0")
elif c == "/" and b != 0:
    print(a / b)
else:
    print("Wrong operation")
