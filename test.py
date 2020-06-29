li = [11, 22, 33, 44, 1, 2, 3, 4, 5, 77, 2, 323, 90]


def func(x):
    return x > 33

# 方式二:filter会自动过滤后面的列表，把列表的第一个元素当成参数传到前面的固定规则函数里面，
# 根据结果是返回true还是false,接着第二个元素，如果是true会根据数据把结果保留下来，如果是false，数据扔掉
# 依次类推，遍历完所有的元素
print('----------list1--------')
new_list1 = filter(func, li)
print(new_list1)
