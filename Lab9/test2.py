dct = {}
x = 0
for i in "2 3 4 5 6 7 8 9 10 J Q K A".split(" "):
    for j in "♣♦♥♠":
        dct[i+j] = x
        x += 1

# print(dct.values())
# print(dct.keys())
# print(dct)

print(list(dct.keys()).index(0))
