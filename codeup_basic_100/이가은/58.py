a, b = map(int, input().split())

a = bool(a)
b = bool(b)

# if a == False and b == False:
#     print(True)
# else:
#     print(False)

print(a == False and b == False)
print(not (a or b))  # ??????
