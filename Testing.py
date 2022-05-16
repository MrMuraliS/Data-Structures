test_lst=[[],
 [],
 [('boy', 20, 23), ('boy', 24, 26)],
 [],
 [('school', 20, 25), ('school', 30, 35)],
 [('jack', 20, 24), ('Mile', 40, 44)]]


def func(val, tar= None):
    if tar is None:
        tar = []
    check = []
    for item in val:
        if item[0] not in check:
            tar.append(item)
            check.append(item[0])
    return tar


final_lst = []

for idx, item in enumerate(test_lst):
    if item and len(item) > 1:
        final_lst.append(func(item))
    else:
        final_lst.append(item)
print(final_lst)