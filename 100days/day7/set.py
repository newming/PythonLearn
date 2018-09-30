# Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

# ![](./res/python-set.png)

def main():
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    print('Length =', len(set1))
    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    print(set1)
    print(set2)
    set2.discard(5) # 使用discard和remove都可以删除set当中的元素，区别就是remove的元素在set当中没有的话会报错，而discard不会。
    # remove的元素如果不存在会引发KeyError
    if 4 in set2:
        set2.remove(4)
    print(set2)
    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print('\n')
    print(set2)
    # # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)
    # 集合的交集、并集、差集、对称差运算
    print(set1 & set2) # 交集
    print(set1.intersection(set2)) # 交集
    print(set1 | set2) # 并集
    print(set1.union(set2)) # 并集
    print(set1 - set2) # 差集 {4, 5}
    print(set1.difference(set2)) # 差集
    print(set1 ^ set2) # 对称差(注意和 差集 的区别) {4, 5, 6, 7, 8, 9, 11, 12}
    print(set1.symmetric_difference(set2)) # 对称差
    # 判断子集和超集
    print(set2 <= set1) # 子集 False
    print(set2.issubset(set1)) # 子集
    print(set3 <= set1) # True
    print(set3.issubset(set1))
    print(set1 >= set2)
    print(set1.issuperset(set2))
    print(set1 >= set3)
    print(set1.issuperset(set3))


if __name__ == '__main__':
    main()

# Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，例如`&`运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。
