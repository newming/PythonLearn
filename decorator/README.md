# 装饰器

```py
# 利用闭包实现的装饰器(这就是装饰器)
def decorator(func):
    def wrapper():
        # do something
        pass
        func()
    return wrapper
```