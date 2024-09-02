from sklearn_pandas import DataFrameMapper
import pandas as pd
import sklearn.preprocessing

data = pd.DataFrame({'pet': ['cat', 'dog', 'fish'], 'age': [5, 7, 2]})

mapper = DataFrameMapper([
    ('pet', sklearn.preprocessing.LabelBinarizer()),
    (['age'], sklearn.preprocessing.StandardScaler())
])

transformed_data = mapper.fit_transform(data)

print(transformed_data)