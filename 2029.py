# import re
# lim = int(input())
# inp = ''.join(reversed(input()[:lim]))
# result = 0
#
# ABC = set("ABC")
# trans = {"A": set("A"), "B": set("B"), "C": set("C")}
# buf_t = trans["A"]
#
# for en, v in enumerate(inp):
#     if v in buf_t:
#         continue
#     else:
#         result += 2 ** (lim - en - 1)
#         buf_t = ABC.difference(trans[v], buf_t)
# print(result)
#
# linp = int(input())
# inp = list(input())[:linp][::-1]
# res = 0
# s_t = "A"
#
# for ind_tow in range(linp):
#     if inp[ind_tow] == s_t:
#         continue
#     else:
#         res += 2**(linp - ind_tow - 1)
#         s_t = "ABC".replace(inp[ind_tow], "").replace(s_t, "")
# print(res)
#

# def doctype():
#     return """
# вот эта хуйня решает задачу
# lim = int(input())
# inp = ''.join(reversed(input()[:lim]))
# result = 0
# ABC = set("ABC")
# trans = {"A": set("A"), "B": set("B"), "C": set("C")}
# buf_t = trans["A"]
#
# for en, v in enumerate(inp):
#     if v in buf_t:
#         continue
#     else:
#         result += 2 ** (lim - en - 1)
#         buf_t = ABC.difference(trans[v], buf_t)
# print(result)
# """
#
#
# def main():
#     """вот эта хуйня запускает строку из хуйни сверху, которая решает задачу"""
#     exec(re.search(string=doctype(),
#                    pattern=r"([^a-я][0-9A-z\W]+)").group(1))

def main() -> int:
    linp = int(input())
    inp = list(input())[:linp][:: - 1]
    res = 0
    s_t = "A"

    for ind_tow in range(linp):
        if inp[ind_tow] == s_t:
            continue
        else:
            res += 2**(linp - ind_tow - 1)
            s_t = "ABC".replace(inp[ind_tow], "")\
                .replace(s_t, "")
    return res


if __name__ == "__main__":
    print(main())
