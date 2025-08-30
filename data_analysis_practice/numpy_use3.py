import numpy as np

# 4 切片操作
# 4.1 一维数组切片
# 一维数组从0开始计数，切片操作是左闭右开[)的。
arr = np.array([1,2,3,4,5])
print(f"arr[1:4]:{arr[1:4]}")

# 4.2 多维数组切片
data=np.array( [
    [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]],
    [[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]]
])
print(f"data:{data}")
print(f"shape:{data.shape}")
print("======")
print(data[0:1])    # data是2*3*5的数组，此行语句取第一个维度的[0:1)的数据，也就是得到了第一个3*5的数组
print("======")
print(data[0:1,0:2])    # 然后对得到的3*5的数组取[0:2)的数据，就得到了一个2*5的数组
print("======")
print(data[0:1,0:2,0:2])    # 然后对得到的2*5的数组在“5”这个维度开刀

# 列切片
print("======")
print(data[:,0:2])  # 第一维的都要，然后从第二维中取
print("======")
print(data[:,:,0:2])    # 第一二维都要，即保留了2*3，然后从第三维中取

# 5 数组堆叠
print("======")
array1=[1,2,3,4,5]
array2=[6,7,8,9,10]
# 垂直堆叠，即建立新维度 两个1*5 -> 一个2*5
print(f"vstack:{np.vstack([array1,array2])}")
# 水平堆叠，即保持原有维度 两个1*5 -> 一个1*10
print(f"hstack:{np.hstack([array1,array2])}")

# 6 保存和加载数组
# 保存数组到文件
np.save('my_array.npy',data)
# 加载数组
loaded_data = np.load('my_array.npy')
