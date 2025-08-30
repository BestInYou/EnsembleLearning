from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

def get_diabetes_data(test_size=0.2, random_state=42, DEBUG=False):
    # 小型回归数据集（用于预测病人的糖尿病指标）
    data = load_diabetes()

    if DEBUG:
        print(data)
    # 将数据集分成训练集和测试集
    # X_train, X_test：特征矩阵，形状是[样本数，特征数]
    # y_train, y_test: 对应的标签值（连续任务，回归任务）
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=test_size, random_state=random_state
    )

    # if DEBUG:
    #     print(X_train)
    #     print(y_train)
    #     print(X_test)
    #     print(y_test)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = get_diabetes_data(DEBUG=True)