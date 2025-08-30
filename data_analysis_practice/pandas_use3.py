import pandas as pd
import openpyxl

# 1 读取数据
df = pd.read_excel('team.xlsx') # 文件在 notebook 文件同一目录下
df.set_index('name', inplace=True) # 建立索引并生效

# 4 分组聚合
print(df.groupby('team').sum()) # 按团队分组对应列相加

print(df.groupby('team').agg({'Q1': 'sum',  # 总和
                        'Q2': 'count', # 总数
                        'Q3':'mean', # 平均
                        'Q4': 'max'})) # 最大值)

# 5 数据转换
# 可以对数据表进行转置
print(df.groupby('team').sum().T)

# 6 增加列
# Pandas增加一列非常方便，就是新定义一个字典的键值一样。
print("===== 6 增加列 =====")
# df['one'] =  1  # 增加一个固定值的列
print(df)
df['total'] = df.Q1 + df.Q2 + df.Q3 + df.Q4 # 增加总成绩列
print(df)
# df['total'] = df.loc[:,'Q1':'Q4'].apply(lambda x:sum(x),axis=1)
# print(df)
df['average'] = df.total/4  # 增加平均成绩列
print(df)

# 7 简单分析
# 根据数据分析目标，试着使用以下函数看看能得到什么结论
# df.mean() # 返回所有列的均值
# df.mean(1) # 返回所有行的均值，下同
# df.corr() # 返回列与列之间的相关系数
# df.count() # 返回每一列中的非空值的个数
# df.max() # 返回每一列的最大值
# df.min() # 返回每一列的最小值
# df.median() # 返回每一列的中位数
# df.std() # 返回每一列的标准差
# df.var() # 方差

# 8 输出
df.to_excel('team_done.xlsx')