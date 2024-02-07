
# n = int(input())
# d = 2
# count = 20
#
# while d * d <= n:
#         if n % d == 0:
#             count -= 1
#             n /= d
#         else:
#             d += 1
# if n > 1:
#     count-=1
#
# if count == 0:
#      print("Yes")
# else:
#      print("No")




#
# def run(n):
#     d = 2
#     count = 20
#     while d * d <= n:
#         while n % d == 0:
#             count -= 1
#             n /= d
#         d += 1
#     if n > 1:
#         count -= 1
#     return count
#
# n = int(input())
# c = run(n)
# if c == 0:
#     print("Yes")
# else:
#     print("No")


# решето всратосфена

# n = int(input())
# a = list(range(n+1))
# print(a)
# a[1] = 0
# i = 2
# while i <= n / 2:
#     if a[i] != 0:
#         j = 2*i
#         while j <= n:
#             a[j] = 0
#             j = j + 1
#     i += 1
#
#
# def eratosthenes(n):     # n - число, до которого хотим найти простые числа
#     sieve = list(range(n + 1))
#     sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
#     for i in sieve:
#         if i > 1:
#             for j in range(2*i, len(sieve), i):
#                 sieve[j] = 0
#     return sieve
# print(eratosthenes(a))
summer = dict.fromkeys([2, 3, 5], 0)
a = 798352691495399040
b = a
# while b > a ** 0.5:

