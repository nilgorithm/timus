# get_vals = [i.split()[1] for i in range(get_vals)]
# d_array = dict()
# l = ["l", "j", "y", "g", "y", "x", "y", "x"]
# b = ["l"]
# c = {k: l.count(k) for k in get_vals}

get_vals = ["Homasho Ishikawa", "Tamakasuga Tokyo", "Futeno Tochigi", "Takekaze Tokyo", "Kasugao Yamaguchi", "Kotoshogiku Ishikawa", "Kotomitsuki Tokyo", "Miyabiyama Shizuoka"]
# extent = int(input())


extent = 3
fighters_quantity = 2 ** extent
aggregated_f = dict()
biggest_gr = 0
raund = 0


for i in range(fighters_quantity):
    town = get_vals[i].split(" ")[1]
    if town in aggregated_f:
        aggregated_f[town] += 1
    else:
        aggregated_f[town] = 1
    if aggregated_f[town] > biggest_gr:
        biggest_gr = aggregated_f[town]


for r in range(extent):
    if biggest_gr > 2 ** (extent - 1):
        break
    elif 2 ** (extent - (r+1)) < biggest_gr <= 2 ** (extent - r):
        break
    else:
        raund += 1
        continue
print(raund)
