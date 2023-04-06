import random as r


def insertSort(lstX):
    # just so we don't change original list
    lst = lstX.copy()
    # just so we don't change original list
    last = lst[-1]

    # print(lst)
    compare = 0
    current = 1
    while True:

        walker = current - 1
        hold = lst.pop(current)
        # print(f"hold = {hold}\nwalker = {walker}")
        # print(lst)
        while walker >= 0 and hold <= lst[walker]:
            compare += 1
            walker -= 1

        lst.insert(walker + 1, hold)

        if hold == last:
            # print(lst)
            print(f"InsertSort Comparing Count : {compare}")
            break

        current += 1
    return lst


def selectionSort(lstX, last=None):
    lst = lstX.copy()

    if last is None:
        last = lst[-1]

    compare = 0
    current = 0

    while True:
        smallest = lst[current]
        walker = current + 1

        while walker < len(lst):
            smallest = min(smallest, lst[walker])
            compare += 1
            walker += 1

        x = lst.index(smallest)
        lst[current], lst[x] = lst[x], lst[current]

        # print(lst)

        if current == len(lst) - 1:
            break

        current += 1

    # print(lst)
    print(f"SelectionSort Compare count : {compare}")
    return lst


def bubbleSort(lstX, last=None):
    lst = lstX.copy()

    if last is None:
        last = len(lst) - 1

    compare = 0
    current = 0
    sorted = False

    while current <= last and not sorted:
        walker = last
        sorted = True

        while walker > current:
            if lst[walker] < lst[walker - 1]:
                sorted = False
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
            compare += 1
            walker -= 1

        current += 1

    print(f"BubbleSortCompare count : {compare}")

    return lst

# insertSort(r.sample(range(1, 100+1),20))
# selectionSort(r.sample(range(1, 101), 20))
# bubbleSort(r.sample(range(1, 10001), 200))


lst10 = [8, 9, 2, 1, 3, 4, 10, 7, 5, 6]

x = r.sample(range(1, 101), 15)

# x = [x for x in range(20, 0, -1)]

print(insertSort(x))
print()
print(selectionSort(x))
print()
print(bubbleSort(x))
