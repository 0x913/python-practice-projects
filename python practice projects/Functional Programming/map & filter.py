

#

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums)) #map

print(result)

res = list(filter(lambda x: x%2==0, nums)) #filter

print(res)