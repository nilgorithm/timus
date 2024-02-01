# def insertion(list_nums: list) -> list:
#     for i in range(1, len(list_nums)):
#         item = list_nums[i]
#         i2 = i - 1
#         while i2 >= 0 and list_nums[i2] > item:
#             list_nums[i2 + 1] = list_nums[i2]
#             i2 -= 1
#         list_nums[i2 + 1] = item
#     return list_nums

def heapify(sort_nums, heap_size, root):
    l = root
    left = (2 * root) + 1
    right = (2 * root) + 2
    if left < heap_size and sort_nums[left] > sort_nums[l]:
        l = left
    if right < heap_size and sort_nums[right] > sort_nums[l]:
        l = right
    if l != root:
        sort_nums[root], sort_nums[l] = sort_nums[l], sort_nums[root]
        heapify(sort_nums, heap_size, l)


def heap(sort_nums: list) -> list:
    size = len(sort_nums)
    for i in range(size, -1, -1):
        heapify(sort_nums, size, i)
    for i in range(size - 1, 0, -1):
        sort_nums[i], sort_nums[0] = sort_nums[0], sort_nums[i]
        heapify(sort_nums, i, 0)
    return sort_nums


input()
al = input().split(" ")
input()
bl = input().split(" ")
input()
cl = input().split(" ")
merge = heap(al + bl + cl)
res = 0

for num in range(len(merge)):
    check = [False if num + i > len(merge)-1 else merge[num] == merge[num + i] for i in range(1, 3)]
    if all(check):
        res += 1
    else:
        continue
print(res)