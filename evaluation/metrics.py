from sklearn.metrics import mean_squared_error, r2_score

def evaluate(model, X_test, y_test):
    # mean_squared_error：均方误差（MSE），误差越小越好
    # r2_score：决定系数，评价预测的“拟合程度”，最大为1，越接近1越好

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2
