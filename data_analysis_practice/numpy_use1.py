import numpy as np
# 1 创建数组
# 1.1 创建一维数组
data1=np.array([1,2,3,4])
print(f"data1:{data1}")

# 1.2 创建二维数组
data2=np.array([[1,2,3,4],[4,5,6,7]])
print(f"data2:{data2}")

# 1.3 创建全0数组
data3 = np.zeros(shape=(2,3))
print(f"data3:{data3}")

# 1.4 创建全1数组
data4 = np.ones(shape=(2,3))
print(f"data4:{data4}")

# 1.5 创建全空数组
data5 = np.empty(shape=(2,3))
print(f"data5:{data5}")

# 1.6 创建有线序序列的数组arange
data6 = np.arange(10,16,2)  # [10,16)的数据，步长为2
print(f"data6:{data6}")

# 1.7 创建有连续间隔的数组linspace
data7 = np.linspace(10,20,11)  # 生成是从 10 到 20 之间生成 11 个等间距的数
print(f"data7:{data7}")

# 1.8 创建随机数组
data8 = np.random.rand(2,3)
print(f"data8:{data8}")
data82=np.random.randint(2,5,size=(4,5))    # 创建一个4行5列，在2到5间取值整数的二位数组
print(f"data82:{data82}")

# 1.9 改变数组形状
data91=[1,2,3,4,5]
data92=[1,2,3,4,5]
data93=np.array([data91,data92])
print("9 改之前的数组形状为:")
print(data93.shape)
data94=data93.reshape((1,10))
print("9 改之后的数组形状为:")
print(data94.shape)

# 1.10 数组转至
data10 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_array = np.array(data10)
print("10 没有转置数组之前数组为：")
print(data10)
print("10 转置数组之后数组为：")
print(data_array.T)
