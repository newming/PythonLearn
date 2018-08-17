# JSON

JSON 是一种轻量级的数据交换格式。字符串是JSON的表现形式。

```python
import json
json.loads(jsonstr)    # 对象的转为了 dict 数组转为了 list
# json 中的 true false 转为 True False

json.dumps(pydict)  # 将 py 对象转为 json
```

转化表：

| json | python |
| ---- | -------|
| object | dice |
| array | list |
| string | str |
| number | int |
| number | float |
| true | True |
| false | False |
| null | None |