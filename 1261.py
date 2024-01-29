#!/usr/bin/python3

from functools import lru_cache
import time

N = int(input())


# time.sleep(N*100/1000)
# l = [(100000,100000)] * (N + 10) * 1024 * 102

@lru_cache(maxsize=None)
def from_two_to_three(n):
    count = 0
    mult = 1
    while n > 0:
        count += (n & 1) * mult
        mult *= 3
        n = n >> 1
    return count


@lru_cache(maxsize=None)
def test_del_three(n):
    if n < 0:
        return False
    return sum(map(int, str(int(n)))) % 3 == 0


@lru_cache(maxsize=None)
def test(n):
    while n > 0:
        if test_del_three(n):
            n = n / 3
        elif test_del_three(n - 1):
            n = (n - 1) / 3
        else:
            return False
    return True


def main(N):
    for i in range(N * 2 + 10):
        payment = from_two_to_three(i)
        if payment > 4294967291:
            print(0)
            return
        if payment > N:
            off = payment - N
            if test(off):
                print(payment, off)
                return (payment, off)
    print(0)


main(N)


# def tests():
#     assert (main(5) == (9, 4))
#     assert (main(528932) == (531444, 2512))
#     assert (main(386891557) == (387423001, 531444))
#     assert (main(19362) == (19686, 324))
#
#
# tests()
