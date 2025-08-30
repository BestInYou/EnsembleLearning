# 导数据分析常用包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 导包获取糖尿病数据集
from sklearn.datasets import load_diabetes
data_diabetes = load_diabetes()

data =  data_diabetes['data']
target = data_diabetes['target']
feature_names = data_diabetes['feature_names']

#现在三个数据都是numpy的一维数据形式，将她们组合成dataframe，可以更直观地观察数据
df =  pd.DataFrame(data,columns = feature_names)
print(df)
