nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

lis = [f"{i} good" if i % 7 == 0 and i % 5 != 0
       else f"{i}" for i in range(1000)]
print(lis)