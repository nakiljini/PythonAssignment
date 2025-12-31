def search(data, searching_item):
    for value in data:
        if value == searching_item:
            break
    else:
        return -1
    return 1

my_list = ['Nakil', 'sharma', 'ifbvh']
print(f"is nakil Present in my_list: {search(my_list, 'Nakil')}")
print(f"is nakilId Present in my_list: {search(my_list, 'NakilId')}")