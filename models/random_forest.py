from sklearn.ensemble import RandomForestRegressor

def train_random_forest(X_train, y_train, n_estimators=100, max_depth=None, random_state=42):
    """
    n_estimators: 森林中树的数量，默认是 100；
    max_depth: 每棵树的最大深度（不设默认表示一直分下去直到叶子纯）；
    random_state: 固定随机数种子，保证每次训练结果一致；
    fit(): 用训练数据训练模型；
    返回训练好的模型。
    """
    # RandomForestRegressor属于Bagging思路的集成模型
    # 它会自动构建多棵决策树，并通过平均多个树的预测结果来输出最终预测值（回归任务中用平均，分类任务中用投票）
    model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)
    return model
