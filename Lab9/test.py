import random

# print(random.sample(range(1, 11), 10))
# x = [8, 9, 2, 1, 3, 4, 10, 7, 5, 6]


# x[0], x[1] = x[1], x[0]
# print(x)

# jik = "♣"
# hrt = "♥"
# dia = "♦"
# bpo = "♠"

dct = {'♣': 'a', '♥': 'b', '♦': 'c', '♠': 'd'}
# print()

lst = ["4♣"]
# hold = '4♠'
# hold = hold[:-1] + dct[hold[-1]]


# print(hold)

# print(lst[0][:-1])
# print(dct[lst[0][-1]])

# print(lst[0][:-1] + dct["A"])

# print(int("10b"))
# .replace("♣", 'a').replace("♥", 'b').replace("♦", 'c').replace("♠", 'd')


# string = "asdasdasdasdsadas"

# ♣ ♥ ♦ ♠

string = "♣♥♦♠"

for i in string:
    print(i, ord(i))

# print(string[:-1].isalpha())

# print(sorted("1 2 3 4 5 6 7 8 9 10 A J K Q".split()))

print("\\".join("10 ♣"))