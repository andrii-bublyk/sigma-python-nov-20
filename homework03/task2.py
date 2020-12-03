search_lambda = lambda l: [i for i in l if len(i) == 6]


test_list1 = ["1", "12", "123", "1234", "12345", "123456", "1234567", "12345678"]
test_list2 = []
test_list3 = ["1", "12", "123", "1234", "12345"]
test_list4 = ["123456", "123456", "123456"]

print(search_lambda(test_list1))
print(search_lambda(test_list2))
print(search_lambda(test_list3))
print(search_lambda(test_list4))
