import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator

class SquareTransformer(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        # fitメソッドでは何もしない（変換器に学習が必要ないため）
        return self

    def transform(self, X):
        # 入力データの2乗を計算
        return np.square(X)
    

import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn_pandas import DataFrameMapper
from sklearn.preprocessing import StandardScaler

class SquareTransformer(TransformerMixin, BaseEstimator):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return np.square(X)

# サンプルデータの作成
data = pd.DataFrame({
    'age': [25, 30, 35],
    'salary': [50000, 60000, 70000]
})

# DataFrameMapperの設定
mapper = DataFrameMapper([
    ('age', SquareTransformer()),  # age列にカスタムTransformerを適用
    (['salary'], StandardScaler())   # salary列にはStandardScalerを適用
])

# データの変換
transformed_data = mapper.fit_transform(data)
print(transformed_data)