from functools import reduce

list =[ [4,8,6,'test'],['jkok', 3, "xz"],[2,7, "best", 4]]

print("The original list : ",str(list))

res = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, str)], list, [])

print("The string values : ", str(res))

res1 = reduce(lambda acc, sublist: acc + [elem for elem in sublist if isinstance(elem, int)], list, [])

print("The int values : ", str(res1))


