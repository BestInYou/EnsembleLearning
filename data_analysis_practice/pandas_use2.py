import pandas as pd
import openpyxl

# 1 读取数据
df = pd.read_excel('team.xlsx') # 文件在 notebook 文件同一目录下
print(df)

# 2 整体数据描述
# df.shape # (100, 6) 查看行数和列数
print(f"df.shape:{df.shape}")

# df.info() # 查看索引、数据类型和内存信息
print(f"df.info:{df.info}")

# df.describe() # 查看数值型列的汇总统计
print(f"df.describe:{df.describe}")

# df.dtypes # 查看各字段类型
print(f"df.dtypes:{df.dtypes}")

# df.axes # 显示数据行和列名
print(f"df.axes:{df.axes}")

# df.index # 查看索引
print(f"df.index:{df.index}")

# df.columns # 列名
print(f"df.columns:{df.columns}")

# 3 建立索引
# 以上数据真正业务意义上的索引是name列，所以我们需要使用它成功索引：
df.set_index('name',inplace=True)   # 建立索引并生效
# 其中可选参数inplace=True会将指定好索引的数据再赋值给df使索引生效，否则不会生效。这并没有对原excel做修改。
print("===== 3 数据将name列设置为索引后 =====")
print(df)

# 4 数据选取（像Excel那样，对数据做一些筛选工作）
# 总体筛选
print("===== 4 数据选取 =====")
print(f"df.head(5):{df.head(5)}")   # 查看DataFrame对象的前5行
print(f"df.tail(5):{df.tail(5)}")
print(f"df.sample(5):{df.sample(5)}")   # 随机5个样本，随机

# 选择列
print(f"df['Q1']:{df['Q1']}")   # 查看Q1列

# 选择行
print(f"df[0:3]:{df[0:3]}]")    # 取前三行
print(f"df[0:10:2]:{df[0:10:2]}")   # 取前十个，每两个取一个
print(f"df.iloc[:10, :]:{df.iloc[:10, :]}")   # 前10个

# 指定行列  loc通过名称或标签来索引，iloc通过索引来寻找数据
print(f"df.loc['Ben','Q1:'Q4']:{df.loc['Ben','Q1':'Q4']}")  # 只看Ben的四个季度成绩
print(f"df.loc['Eorge':'Alexander','team':'Q4']:{df.loc['Eorge':'Alexander','team':'Q4']}") # 指定行区间

# 排序
df.sort_values('Q1')    # 按Q1列数据升序排序
print(f"df.sort_values('Q1'):{df}")
df.sort_values('Q1', ascending=False)   # 降序
print(f"df.sort_values('Q1',ascending=False):{df}")
df.sort_values(['team','Q1'], ascending=[True, False])  # team升，Q1降

# 条件选择
# 单一条件
print(f"df[df.Q1>90]:{df[df.Q1>90]}")   # 列大于90的
print(f"df[df.team=='C']:{df[df.team=='C']}")  # team列为'C'的
# 组合条件
print(df.sort_values(by='Q1')) # 按 Q1 列数据升序排列
print(df.sort_values(by='Q1', ascending=False)) # 降序

print(df.sort_values(['team', 'Q1'], ascending=[True, False])) # team 升，Q1 降序
