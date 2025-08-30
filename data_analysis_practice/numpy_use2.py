import numpy as np

# 2 数组显示操作
# 2.1 数组维度ndim
data1 = np.array([[1,2,3,4],
                  [5,6,7,8]])
print(f"data1.ndim:{data1.ndim}")

# 2.2 数组形状shape
print(f"data1.shape:{data1.shape}")

# 2.3 数组中元素个数
print(f"data1.size:{data1.size}")

# 2.4 数组的数据类型
print(f"data1.dtype:{data1.dtype}")

# 3 数组的运算
# 3.1 加法
data2 = np.array([[1,2,3,4],
                  [5,6,7,8]])
print(f"data1+data2:{data1+data2}")
# 3.2 乘法
print(f"data1*data2:{data1*data2}")

# 3 数组中的统计操作
# 数据统计有个印象就行，不要刻意的去记，用到的时候回来看一眼就可以了，多用也就会了
# 3.1 计算数组中的平均值
# numpy.mean(arr,axis=None,dtype=None,out=None):计算数组的平均值
# 参数：axis表示沿着哪个轴进行计算，默认为None，表示计算整个数组的平均值；
#       dtype表示返回结果的数据类型，默认为float64;
#       out表示将结果存储在指定的数组中，一般情况下，传个数组进去就可以了
print(f"mean:{np.mean(data1,axis=1)}")

# 3.2 计算中位数
print(f"median:{np.median(data1,axis=0)}")

# 剩下的不演示了：参数大致都相同
# 标准差：np.std()
# 方差：np.var()
# 最小值：np.min()
# 最大值：np.max()
# 元素之和：np.sum()
# 元素乘积：np.prod()
# 累计和：np.cumsum()