# LightGBM回归模型

## 作者：ShuHang2

[![build](https://github.com/Anduin2017/HowToCook/actions/workflows/build.yml/badge.svg)](https://github.com/ShuHang2/ShuHang2.github.io)

## [返回主页](../README.md)

## 天气预测

### 参考链接

项目代码仓库地址：[天气预测及房价预测代码](https://github.com/ShuHang2/LGBM_XGB)

机器学习比赛流程了解：[数据科学竞赛：你从未见过的究极进化秘笈](https://zhuanlan.zhihu.com/p/149769029?utm_campaign=shareopn&utm_medium=social&utm_oi=1426176965909377024&utm_psn=1647744152111656960&utm_source=wechat_session)

LightGBM官方文档：[lightgbm.LGBMRegressor](https://lightgbm.readthedocs.io/en/latest/pythonapi/lightgbm.LGBMRegressor.html)

LightGBM视频参考：[30行代码 = 排行榜前5%, Kaggle 房价预测项目, 分享我的 LightGBM 极简工作流.](https://www.bilibili.com/video/BV13H4y1B7ma/?spm_id_from=333.337.search-card.all.click&vd_source=4ccf948892d4f576c919af8b39cbe8dc)

### LightGBM回归

#### 导入基础库

```python
import pandas as pd
import numpy as np
```

### 数据分析

#### 对数据集进行导入，并查看数据集的大小

```python
train = pd.read_csv("./data/train.csv")
test = pd.read_csv("./data/test.csv")

print("train size:", train.shape)
print("test size:", test.shape)
```

#### 查看数据缺失值百分比

通过查看 csv 文件中，我们能明显的看出有大量的数据缺失，我们写一个函数对数据的缺失值进行查看。

我们使用isnull 函数对空值进行统计，再除以总行数，得出缺失值占比

```python
import pandas as pd

def missing_value_percent(train):
    missing_values_count = train.isnull().sum()
    total_values = train.shape[0]
    missing_values_percentage = (missing_values_count / total_values) * 100
    print(missing_values_percentage)

missing_value_percent(train)
```

### 数据清洗

#### 处理缺失数值类型的数据

根据数据缺失值的具体情况，由于天气数据是以时间顺序进行排列，我们挑选出数据缺失值较少且为数值型的使interpolate 函数进行线性插值，补全数据。

```python
# missing number value 
columns_miss = [
    "WindGustSpeed",
    "WindSpeed9am",
    "WindSpeed3pm",
    "Humidity9am",
    "Humidity3pm",
    "Pressure9am",
    "Pressure3pm",
    "Temp9am",
    "Temp3pm",
    "MinTemp",
    "MaxTemp",
    "Rainfall"
]

for column in columns_miss:
    train[column] = train[column].interpolate(method="linear")

missing_value_percent(train)
```

#### 处理缺失Object（String）类型的数据

我们在挑选出，数值缺失较少的非数值类型的，进行前后插值

```python
columns_miss_object = ["RainToday", "RainTomorrow"]

for column in columns_miss_object:
    train[column] = train[column].ffill().bfill()

missing_value_percent(train)
```

#### 数据集合并

LightGBM模型只能输入数值类型的数据，我们挑选出Obkect类型的数据

```python
# union dataset, cherk object and null data
xy_all = pd.concat([train, test], axis=0)
cat_features = [
    "Date",
    "Location",

    "WindGustDir",
    "WindDir9am",
    "WindDir3pm",

    "RainToday",
    "RainTomorrow",

    "Evaporation",
    "Sunshine",
    "Cloud9am",
    "Cloud3pm",
]

print("features:", cat_features, "\n length:", len(cat_features))
print("xy_all size:", xy_all.shape)
```

### 特征工程

#### 数据处理

对于缺失值缺失太多的数据，因为有大段的缺失，使用数据补全的效果很差，就不进行数据补全，而将它置为-1 表示为空值

我们使用 OrdinalEncoder 将缺失值转化为-1，将非数值型映射到唯一且输定的数。并对其进行归一化。通过归一化，我们的目标 RainTomorrow，下雨就是 1，不下雨就是 0

```python
# processing value
# object(string) type to in32, NAN and missing value to -1
from sklearn.preprocessing import OrdinalEncoder

ordinal_encoder = OrdinalEncoder(
    dtype=np.int64,
    handle_unknown="use_encoded_value",
    unknown_value=-1,
    encoded_missing_value=-1
).set_output(transform="pandas")

xy_all[cat_features] = ordinal_encoder.fit_transform(xy_all[cat_features])
print("xy_all size:", xy_all.shape)
```

#### 数据分割

由于我们是将训练集和测试集，一起进行特征处理，我们需要再将他们进行分开。我们通过 RainTomorrow 为 -1 就是 x_test。RainTomorrow 不是 -1 就是xy_train。

从而，将训练集的特征和目标分开。

```python
# Split
# RainTomorrow with -1 is x_test
# RainTomorrow without -1 is xy_train

xy_train = xy_all[xy_all["RainTomorrow"] != -1]
x_train = xy_train.drop(columns=["RainTomorrow"])
y_train = xy_train["RainTomorrow"]
x_test = xy_all[xy_all["RainTomorrow"] == -1].drop(columns="RainTomorrow")
```

### 建模

#### 导入LightGBM模型

一开始可以使用默认参数，这个参数可以通过[参数查找函数](寻参函数.md)进行查找

```python
import lightgbm as lgb
model = lgb.LGBMRegressor(
    boosting_type="gbdt",
    num_leaves=74,
    max_depth=-1,
    learning_rate=0.09794344673376235,
    n_estimators=380,
    subsample_for_bin=200000,
    objective=None,
    class_weight=None,
    min_split_gain=0.0,
    min_child_weight=0.001,
    min_child_samples=67,
    subsample=0.8447134830762376,
    subsample_freq=0,
    colsample_bytree=0.9337489793588183,
    reg_alpha=0.8447134830762376,
    reg_lambda=0.8447134830762376,
    random_state=42,
    n_jobs=None,
    importance_type="split",
)
```

### 模型训练

```python
model.fit(x_train, y_train)
```

### 模型预测

因为我使用的是回归模型，所以我们需要将数值转化为 Yes 或 No

```python
# predict
y_pred = model.predict(x_test)
y_pred_str = np.where(y_pred > 0.5, "Yes", "No")
```

#### 预测结果保存为CSV文件

```python
# save csv
pd.DataFrame({
    "id": x_test["id"],
    "RainTomorrow": y_pred_str
}).to_csv("./output/LGBM.csv", index=False)
```

### 模型结合

xgboost的使用方法和LightGBM一模一样

我使用 lightgbm 和 xgboost 模型进行结合，因为这两个模型的预测结果评分
较好。

将其结合，希望有更好的分数。我使用简单加权平均将逻辑回归的结果相加，再
除二，将结果通过判断映射到 Yes 或 No

也可以使用Bagging、Boosting方法等

```python
y_pred = 0.5 * y_lgbm_pred + 0.5 * y_xgb_pred
```
