from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd
import os

def grid_search_rf(X_train, y_train, cv=5, save_path="grid_search_results.csv"):
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [10, 15, 20, None],
        'min_samples_split': [2, 5],
        'min_samples_leaf': [1, 2],
        'max_features': ['sqrt', 'log2']
    }

    model = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(model, param_grid, cv=cv, scoring='r2', n_jobs=-1, return_train_score=True)
    grid_search.fit(X_train, y_train)

    # === 保存结果到 CSV（追加或创建）
    results_df = pd.DataFrame(grid_search.cv_results_)
    results_df = results_df[[
        'params', 'mean_test_score', 'mean_train_score', 'rank_test_score'
    ]].sort_values(by='rank_test_score')

    # 追加模式保存（避免重复写头部）
    if os.path.exists(save_path):
        existing = pd.read_csv(save_path)
        combined = pd.concat([existing, results_df], ignore_index=True)
        combined.drop_duplicates(subset=['params'], inplace=True)
        combined.to_csv(save_path, index=False)
    else:
        results_df.to_csv(save_path, index=False)

    return grid_search.best_estimator_, grid_search.best_params_, grid_search.best_score_
