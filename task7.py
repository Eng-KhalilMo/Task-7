# 1

# my_dict = {'name': 'Ahmed', 'age': 20, 'job': 'Engineer'}
#
# print(list(my_dict.values()))
#
# print(list(my_dict.keys()))
#
# print(my_dict['name'])
#
# my_dict['age'] = 32
#
# my_dict['Workplace'] = 'GSG'
#
# print(my_dict)


# 2

# my_tuple = (('name', 'Ahmed'), ('age', 23), ('job', 'Doctor'))
#
# my_dict = {}
#
# for key, value in my_tuple:
#     my_dict[value] = key
#
# print(my_dict)


# 3

# dic1 = {'name': 'Dema', 'age': 20}
# dic2 = {'job': 'Engineer', 'ID': 456367}
# dic3 = {'Year': 2003}
#
# new_dict = {**dic1, **dic2, **dic3}
#
# print(new_dict)


# 4

# my_dict = {'num1': 648, 'num2': 4194, 'num3': 60}
#
# max_value = max(my_dict.values())
#
# min_value = min(my_dict.values())
#
# print("Maximum Value:", max_value)
# print("Minimum Value:", min_value)


# 5

# my_dict = {'name': 'Abed', 'age': 31, 'job': 'Teacher'}
#
# key_exists = 'ID' in my_dict
#
# print(key_exists)


# 6

# Languages2023 = {'Programming Language': ['python', 'Java', 'JavaScript', 'C#'],
#                  'Market Share %': [27.99, 15.9, 9.36, 6.67]}
#
# programming_languages = Languages2023['Programming Language']
# market_share_percentages = Languages2023['Market Share %']
#
# result_list = [{'Programming Language': lang, 'Market Share %': share}
#                for lang, share in zip(programming_languages, market_share_percentages)]
#
# for item in result_list:
#     print(item)
