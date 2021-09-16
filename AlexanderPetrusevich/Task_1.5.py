main_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
unique_list = list(set(val for dic in main_list for val in dic.values()))
print(unique_list)