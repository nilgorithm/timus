#!/usr/bin/python3

import sys

# def test0():
#     assert(main(4, 3, ((3,2),(3,1),(1,4))) == 2)
#     print('test0 is Ok')
#
# def test1():
#     paths = (
#             (1,2),
#             (2,6),
#             (3,2),
#             (4,2),
#             (5,3),
#             (6,7),
#             (7,8),
#             (9,7),
#             )
#     assert(main(9, 6, paths) == None)
#     print('test1 is Ok')
#
# def test2():
#     paths = (
#             (1,2),
#             (2,6),
#             (3,2),
#             (4,2),
#             (5,3),
#             (6,7),
#             (7,8),
#             (9,7),
#             )
#     print(main(9, 1, paths))
#     assert(main(9, 1, paths) == None)
#     print('test2 is Ok')

sys.setrecursionlimit(10000)


def main(n, k, paths):
    airbases = list(range(1, n+1))
    start = k
    lines = {}
    for ap in paths: # ap - airports
        for i, j in zip([0,1],[1,0]):
            if ap[i] in lines:
                lines[ap[i]].add(ap[j])
            else:
                lines[ap[i]] = set([ap[j]])

    def ok_lets_go(not_bombed, pos, step):
        if pos not in lines:
            return step % 2 != 1
        test_lines = []
        for to in lines[pos].intersection(not_bombed):
            new_not_bombed = not_bombed.difference(set([pos]))
            test_lines.append(ok_lets_go(new_not_bombed, to, step+1))
        if len(test_lines) == 0:
            return step % 2 == 1
        if step % 2 == 1:
            return all(test_lines)
        return any(test_lines)

    ok = []
    for to in lines[start]:
        not_bombed = set(lines.keys()).difference(set([start]))
        if ok_lets_go(not_bombed, to, 1):
            ok.append(to)
    if len(ok) > 0:
        return min(ok)
    return None

def test_in():
    n, k = input().split()
    n = int(n)
    k = int(k)
    paths = []
    for _ in range(n-1):
        i, j = input().split()
        paths += [(int(i), int(j))]
    try:
        res = main(n, k, paths)
    except RecursionError:
        res = None
    if res is None:
        print('First player loses')
    else:
        print(f'First player wins flying to airport {res}')

test_in()
