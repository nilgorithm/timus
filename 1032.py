def main():
    n = int(input())
    # n = 5
    # arr = [1, 2, 3, 4, 1]
    arr = []
    s = 0
    summarize = [0]
    for i in range(n):
        numb = int(input())
        arr.append(numb)
        s += numb
        # s += arr[i]
        summarize.append(s)

    # print(arr)
    # print(summarize)
    res = False
    for i in range(n+1):
        if not res:
            for j in range(i):
                if (summarize[i]-summarize[j]) % n == 0:
                    # print(summarize[i], summarize[j])
                    print("i-j",  i-j)
                    res = True
                    for k in range(j, i):
                        # print("index", i)
                        print("arr[k]", arr[k])
                        # print(arr[k])
        else:
            break
    if not res:
        print(0)

# main()


# n = int(input())
# arr = []
# s = 0
# summarize = [0]
# for i in range(n):
#     numb = int(input())
#     arr.append(numb)
#     s += numb
#     summarize.append(s)
# run = True
# for i in range(n+1):
#     if run:
#         for j in range(i):
#             if (summarize[i]-summarize[j]) % n == 0 and run:
#                 print(i-j)
#                 run = False
#                 for k in range(j, i):
#                     print(arr[k])
#                     # print("arr[k]", arr[k])
#             elif not run:
#                 break
#     else:
#         break
# if run:
#     print(0)

N = int(input())
A = [int(input()) for i in range(N)]

used = [0] + [-1] * 9999
sum_val = 0

for i in range(N):
    sum_val += A[i]

    if used[sum_val % N] != -1:
        print(i - used[sum_val % N] + 1)
        for j in range(used[sum_val % N], i + 1):
            print(A[j])
        break
    else:
        used[sum_val % N] = i + 1