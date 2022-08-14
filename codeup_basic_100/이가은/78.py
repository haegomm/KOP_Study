a = input()

if a != 'q':
    while a != 'q':
        print(a)
        a = input()

        if a == 'q':
            print(a)
            break
else:
    print(a)


while True:
    x = input()
    print(x)
    if x == 'q':
        break
