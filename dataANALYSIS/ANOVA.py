# 导入必要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 设置中文字体
# plt.rcParams['font.sans-serif'] = ['SimHei']
import seaborn as sns
from scipy.stats import chi2_contingency, f_oneway, pearsonr
from sklearn.linear_model import LinearRegression
from matplotlib.ticker import FuncFormatter

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
    print(f"卡方检验结果：{feature}和{target}之间的卡方值为{chi2:.2f}，p值为{p:.4g}，自由度为{dof}")
    list.append({'feature': feature, 'chi2': chi2, 'p': p, 'dof': dof})
    # 根据p值判断是否拒绝原假设
    if p < 0.05:
        print(f"结论：拒绝原假设，{feature}和{target}之间有显著关联性")
    else:
        print(f"结论：不能拒绝原假设，{feature}和{target}之间没有显著关联性")
    print()

def y_update_scale_value(temp, position):
    return "$10^{{{}}}$".format(temp)

# visualization p in Log Bar
colors = ['#D6594C']
list = sorted(list, key=lambda x: x['p'])
df = pd.DataFrame(list)
# print(df['p'])
df['p'] = [np.log10(x) for x in df['p']]
plt.figure(figsize=(9, 6))
sns.barplot(x="feature",y='p', data=df, palette = colors,width=0.5)
plt.ylabel('P value (log scale)')
plt.xlabel('')
plt.gca().yaxis.set_major_formatter(FuncFormatter(y_update_scale_value))
plt.rc('axes', unicode_minus=False)
plt.title('Chi-square P value')

# 对每个定量特征和目标变量进行方差分析
list = []
for feature in numerical_features:
    # 分组数据
    group1 = data[data[target] == 0][feature]
    group2 = data[data[target] == 1][feature]
    # 计算F值和p值
    F, p = f_oneway(group1, group2)
    # 打印结果
    print(f"方差分析结果：{feature}和{target}之间的F值为{F:.2f}，p值为{p:.4g}")
    list.append({'feature': feature, 'F': F, 'p': p})
    # 根据p值判断是否拒绝原假设
    if p < 0.05:
        print(f"结论：拒绝原假设，{feature}和{target}之间有显著差异")
    else:
        print(f"结论：不能拒绝原假设，{feature}和{target}之间没有显著差异")
    print()

plt.figure(figsize=(9, 6))
colors = ['#D6594C']
list = sorted(list, key=lambda x: x['p'])
df = pd.DataFrame(list)
print(df['p'])
df['p'] = [np.log10(x) for x in df['p']]
sns.barplot(x="feature",y='p', data=df, palette = colors,width=0.5)
plt.ylabel('P value (log scale)')
plt.xlabel('')
plt.gca().yaxis.set_major_formatter(FuncFormatter(y_update_scale_value))
plt.title('ANOVA P value')
plt.show()
