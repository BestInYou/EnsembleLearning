from data.load_data import get_diabetes_data
from models.grid_search import grid_search_rf
from visualization.plot_results import plot_predictions
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # 1、加载数据
    X_train, X_test, y_train, y_test = get_diabetes_data()

    # 2、网格搜索 + 训练模型
    model, best_params, best_cv_score = grid_search_rf(X_train, y_train)
    print(f"[GridSearch] Best Params: {best_params}")
    print(f"[GridSearch] Best CV R^2 Score: {best_cv_score:.2f}")

    # 3、预测与评估
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"\n[Final Evaluation on Test Set]")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R^2 Score: {r2:.2f}")

    # 4、可视化
    plot_predictions(y_test, y_pred)

if __name__ == "__main__":
    main()
