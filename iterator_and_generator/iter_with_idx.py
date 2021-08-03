my_list = ['a', 'b', 'c']

# enumerate(iter, startidx)
for idx, i in enumerate(my_list, 1):
    print('idx-{} : {}'.format(idx, i))
