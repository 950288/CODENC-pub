# 导入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
import seaborn as sns
from scipy.stats import chi2_contingency, f_oneway, pearsonr
from sklearn.linear_model import LinearRegression

# 读取数据
data = pd.read_csv("heart.csv")

# 定义定类特征和定量特征的列表
categorical_features = ["Sex", "ChestPainType", "FastingBS", "RestingECG", "ExerciseAngina", "ST_Slope"]
numerical_features = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]

# 定义目标变量
target = "HeartDisease"

list = []
# 对每个定类特征和目标变量进行卡方检验
for feature in categorical_features:
    # 构建列联表
    contingency_table = pd.crosstab(data[feature], data[target])
    # 计算卡方值，p值，自由度和期望频数
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    # 打印结果
    print(f"卡方检验结果：{feature}和{target}之间的卡方值为{chi2:.2f}，p值为{p:.10g}，自由度为{dof}")
    list.append({'feature': feature, 'chi2': chi2, 'p': p, 'dof': dof})
    # 根据p值判断是否拒绝原假设
    if p < 0.05:
        print(f"结论：拒绝原假设，{feature}和{target}之间有显著关联性")
    else:
        print(f"结论：不能拒绝原假设，{feature}和{target}之间没有显著关联性")
    print()

# visualization p in Log Bar
# reorder the list by p
list = sorted(list, key=lambda x: x['p'])
df = pd.DataFrame(list)
df['p'] = np.log10(df['p'])
plt.figure(figsize=(10, 6))
sns.barplot(x='feature', y='p', data=df)
plt.xlabel('feature')
plt.ylabel('p')
plt.title('p in Log Bar')
plt.show()




# 对每个定量特征和目标变量进行方差分析
for feature in numerical_features:
    # 分组数据
    group1 = data[data[target] == 0][feature]
    group2 = data[data[target] == 1][feature]
    # 计算F值和p值
    F, p = f_oneway(group1, group2)
    # 打印结果
    print(f"方差分析结果：{feature}和{target}之间的F值为{F:.2f}，p值为{p:.4g}")
    # 根据p值判断是否拒绝原假设
    if p < 0.05:
        print(f"结论：拒绝原假设，{feature}和{target}之间有显著差异")
    else:
        print(f"结论：不能拒绝原假设，{feature}和{target}之间没有显著差异")
    print()

# 对每个定量特征和目标变量进行相关分析或回归分析
# for feature in numerical_features:
#     # 计算相关系数和p值
#     r, p = pearsonr(data[feature], data[target])
#     # 打印结果
#     print(f"相关分析结果：{feature}和{target}之间的相关系数为{r:.2f}，p值为{p:.4f}")
#     # 根据p值判断是否拒绝原假设
#     if p < 0.05:
#         print(f"结论：拒绝原假设，{feature}和{target}之间有显著线性关系")
#         # 进行回归分析
#         # 定义自变量和因变量
#         X = data[feature].values.reshape(-1, 1)
#         y = data[target].values
#         # 创建线性回归模型
#         model = LinearRegression()
#         # 拟合数据
#         model.fit(X, y)
#         # 获取回归系数和截距
#         coef = model.coef_[0]
#         intercept = model.intercept_
#         # 打印回归方程
#         print(f"回归分析结果：{target} = {coef:.2f} * {feature} + {intercept:.2f}")
#         # 绘制散点图和回归线
#         plt.scatter(X, y, label="数据点")
#         plt.plot(X, model.predict(X), color="red", label="回归线")
#         plt.xlabel(feature)
#         plt.ylabel(target)
#         plt.legend()
#         plt.show()
#     else:
#         print(f"结论：不能拒绝原假设，{feature}和{target}之间没有显著线性关系")
#     print()
