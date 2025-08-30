import numpy as np
import pandas as pd

# 1、对象创建
# 1.1 创建Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(f"s:{s}")

# 1.2 通过传入Numpy数组，使用data_range()创建带有日期时间索引和标签列的DataFrame
dates = pd.date_range("20130101", periods=6)
print(f"dates:{dates}")
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(f"df:{df}")

# 1.3 通过传入一个对象字典创建DataFrame，其中健是列标签，值是列值
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(f"df2:{df2}")

# 2 查看数据
# 2.1 使用DataFrame.head()和DataFrame.tail()分别查看框架的顶部和底部行
print(f"df2.head():{df2.head()}")
print(f"df2.tail():{df2.tail()}")