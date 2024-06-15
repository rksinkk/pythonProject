my_dict = {'a': 2, 'b': 1, 'c': 3}
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)