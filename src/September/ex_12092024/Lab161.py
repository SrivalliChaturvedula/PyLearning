# ordered dictionary - dictionary that remembers order

from collections import OrderedDict, defaultdict

# normal dict
dict = dict()
dict["age"] = 32
dict["name"] = "Valli"
dict["id"] = 43
dict["address"] = "HYD"
print(dict)

# ordered dict
od = OrderedDict()
od["banana"] = 2
od["apple"] = 3
od["pear"] = 4
print(od)

dd = defaultdict(int)
print(dd)