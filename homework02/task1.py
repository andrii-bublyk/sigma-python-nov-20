begin_of_range = 1000
end_of_range = 1500

for i in range(begin_of_range, end_of_range + 1):
    if (i % 3 == 0) and (i % 8 == 0):
        print(i)
