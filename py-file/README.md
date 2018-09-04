# python 文件操作

## 文件打开方式

open(name[, mode[buf]])

- name: 文件路径
- mode: 打开方式
- buf: 缓冲 buffering 大小

| mode | 说明 | 注意 |
| ---- | ---- | ---- |
| r | 只读方式打开 | 文件必须存在 |
| w | 只写方式打开 | 文件不存在则创建文件，文件存在则清空文件内容 |
| a | 追加方式打开 | 文件不存在则创建文件 |
| r+/w+ | 读写方式打开 |  |
| a+ | 追加和读写方式打开 |  |
| rb/wb/ab/rb+/wb+/ab+ | 二进制方式打开 |  |

## 读取文件

- read([size]): 读取文件(读取 size 个字节，默认读取完)
- readline([size]): 读取一行
- readlines([size]): 读取完文件，返回每一行所组成的列表

## 写入文件

- write(str): 将字符串写入文件
- writelines(sequence_of_strings): 写多行到文件

# 关闭文件

close()