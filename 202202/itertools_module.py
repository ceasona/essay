from itertools import cycle, groupby, islice, permutations, combinations

# cycle, 无限的迭代器
# groupby,
# islice, 返回一个迭代器中的一段内容
# permutations, 排列
# combinations, 组合

print(list(islice(cycle('abcd'), 0, 11)))

animals_1 = ['pig', 'cow', 'giraffe', 'elephant',
             'dog', 'cat', 'hippo', 'lion', 'tiger']
animals_2 = sorted(['pig', 'cow', 'giraffe', 'elephant',
                    'dog', 'cat', 'hippo', 'lion', 'tiger'], key=len)
print(animals_1)
# 按照长度进行分组
for k, g in groupby(animals_1, key=len):
    print(k, list(g))
print("*" * 12)
print(animals_2)
for k, g in groupby(animals_2, key=len):
    print(k, list(g))

print("*" * 12)
for p in permutations('abc'):
    print(p)

print("*" * 12)
print([list(c) for c in combinations([1, 2, 3, 4], r=2)])
