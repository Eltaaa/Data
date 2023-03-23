from time import time


def loopSummation(num):
    """ loop """
    ans = 0

    for i in range(1, num+1):
        ans += i

    return ans


def summation(num):
    return num * (num + 1) / 2


def analyze(num):
    print(num)
    starttime = time()
    loopSummation(num)
    endtime = time()
    print("Loop Elapse :", (endtime - starttime))

    starttime = time()
    summation(num)
    endtime = time()
    print("     Elapse :", (endtime - starttime))

    print("========")


analyze(100) # 100
analyze(10_000) # 10K
analyze(1_000_000) # 1M
analyze(100_000_000) # 100M
analyze(1_000_000_000) # 1B