a = int(input('первый день'))
b = int(input('конечный итог'))
n = 1
while a <= b:
    print(n, '-ый день:', a)
    a = (a + (a * 0.1))
    n = n + 1

    if a > b:
        print(n, '-ый день:', a)
        break
   







