data = [line.strip() for line in open("day1_input.txt").readlines()]

arr1 = sorted([int(d.split()[0]) for d in data])
arr2 = sorted([int(d.split()[1]) for d in data])

total = sum(abs(a - b) for a, b in zip(arr1, arr2))
print(total)

#part_2
data = [line.strip() for line in open("day1_input.txt").readlines()]

arr1 = [int(d.split()[0]) for d in data]
dict2 = {}
for d in [int(d.split()[1]) for d in data]:
    dict2[d] = dict2.get(d, 0) + 1

sim = sum([n * dict2.get(n, 0) for n in arr1])

print(sim)