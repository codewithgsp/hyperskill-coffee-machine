cafe_name_lists = []
count_lists = []
while True:
    details = input().split()
    if len(details) == 2:
        cafe_name_lists.append(details[0])
        count_lists.append(int(details[1]))
    else:
        break
max_cat_num = max(count_lists)
max_cat_index = count_lists.index(max_cat_num)
print(cafe_name_lists[max_cat_index])
