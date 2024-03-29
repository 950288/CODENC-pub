import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
pd.options.display.float_format = '{:.2f}'.format
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('./heart.csv')
data.head()

# print(data.shape)
# print(data.columns)
# print(data.info())

sns.heatmap(data.isnull(),cmap = 'magma',cbar = False)

print("-----------data imported-----------")

print(data.describe().T)

yes = data[data['HeartDisease'] == 1].describe().T
no = data[data['HeartDisease'] == 0].describe().T
colors = ['#FABB6E','#508AB2']

# fig, ax = plt.subplots(nrows = 1,ncols = 2,figsize = (5,5))
# plt.subplot(1,2,1)
# sns.heatmap(yes[['mean']],annot = True,cmap = colors,linewidths = 0.4,linecolor = 'black',cbar = False,fmt = '.2f',)
# plt.title('Heart Disease')

# plt.subplot(1,2,2)
# sns.heatmap(no[['mean']],annot = True,cmap = colors,linewidths = 0.4,linecolor = 'black',cbar = False,fmt = '.2f')
# plt.title('No Heart Disease')

# fig.tight_layout(pad = 2)

# plt.show()

# Exploratory Data Analysis

col = list(data.columns)
categorical_features = []
numerical_features = []
for i in col:
    if len(data[i].unique()) > 6:
        numerical_features.append(i)
    else:
        categorical_features.append(i)

print('Categorical Features :',*categorical_features) # 这些数据是离散的
print('Numerical Features :',*numerical_features) # 这些数据是连续的

# 离散数据的分布
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df1 = data.copy(deep = True)

df1['Sex'] = le.fit_transform(df1['Sex'])
df1['ChestPainType'] = le.fit_transform(df1['ChestPainType'])
df1['RestingECG'] = le.fit_transform(df1['RestingECG'])
df1['ExerciseAngina'] = le.fit_transform(df1['ExerciseAngina'])
df1['ST_Slope'] = le.fit_transform(df1['ST_Slope'])

# fig, ax = plt.subplots(nrows = 3,ncols = 2,figsize = (10,15))
# for i in range(len(categorical_features) - 1):
    
#     plt.subplot(3,2,i+1)
#     sns.distplot(df1[categorical_features[i]],kde_kws = {'bw' : 1},color = colors[0])
#     title = 'Distribution : ' + categorical_features[i]
#     plt.title(title)
    
# plt.figure(figsize = (4.75,4.55))
# sns.distplot(df1[categorical_features[len(categorical_features) - 1]],kde_kws = {'bw' : 1},color = colors[0])
# title = 'Distribution : ' + categorical_features[len(categorical_features) - 1]
# plt.title(title)

# 连续数据的分布
fig, ax = plt.subplots(nrows = 3,ncols = 2,figsize = (6,5))
for i in range(len(numerical_features)):
    plt.subplot(3,2,i+1)
    sns.distplot(data[numerical_features[i]],color = colors[0])
    title = 'Distribution : ' + numerical_features[i]
    plt.title(title)
# plt.show()
plt.tight_layout()

# plt.figure(figsize = (4.75,4.55))
# sns.distplot(df1[numerical_features[len(numerical_features) - 1]],kde_kws = {'bw' : 1},color = colors[0])
# title = 'Distribution : ' + numerical_features[len(numerical_features) - 1]
# plt.title(title)

# Target Variable Visualization (HeartDisease)
# l = list(data['HeartDisease'].value_counts())
# circle = [l[1] / sum(l) * 100,l[0] / sum(l) * 100]

# fig, ax = plt.subplots(nrows = 1,ncols = 2,figsize = (20,5))
# plt.subplot(1,2,1)
# plt.pie(circle,labels = ['No Heart Disease','Heart Disease'],autopct='%1.1f%%',startangle = 90,explode = (0.1,0),colors = colors,
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('Heart Disease %')

# plt.subplot(1,2,2)
# ax = sns.countplot(x='HeartDisease',data = data,palette = colors,edgecolor = 'black')
# for rect in ax.patches:
#     ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2, rect.get_height(), horizontalalignment='center', fontsize = 11)
# ax.set_xticklabels(['No Heart Disease','Heart Disease'])
# plt.title('Cases of Heart Disease')

# plt.show()

# Categorical Features vs Target Variable (HeartDisease) 
fig, ax = plt.subplots(nrows = 2,ncols = 3,figsize = (12,8))
for i in range(len(categorical_features) - 1):
    plt.subplot(2,3,i+1)
    ax = sns.countplot(x=categorical_features[i],data = data,hue = "HeartDisease",palette = colors,edgecolor = 'black')
    for rect in ax.patches:
        if rect.get_height() > 0:
            ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2, rect.get_height(), horizontalalignment='center', fontsize = 11)
    title = categorical_features[i] + ' vs HeartDisease'
    print(title)
    plt.legend(['No Heart Disease','Heart Disease'])
    plt.title(title)
    y_num = data[categorical_features[i]].value_counts()
    plt.ylim(0, max(y_num))
    # print(data[categorical_features[i]].value_counts())
plt.tight_layout()


# Categorical Features vs Positive Heart Disease Cases pie chart
# sex = data[data['HeartDisease'] == 1]['Sex'].value_counts()
# sex = [sex[0] / sum(sex) * 100, sex[1] / sum(sex) * 100]

# cp = data[data['HeartDisease'] == 1]['ChestPainType'].value_counts()
# cp = [cp[0] / sum(cp) * 100,cp[1] / sum(cp) * 100,cp[2] / sum(cp) * 100,cp[3] / sum(cp) * 100]

# fbs = data[data['HeartDisease'] == 1]['FastingBS'].value_counts()
# fbs = [fbs[0] / sum(fbs) * 100,fbs[1] / sum(fbs) * 100]

# restecg = data[data['HeartDisease'] == 1]['RestingECG'].value_counts()
# restecg = [restecg[0] / sum(restecg) * 100,restecg[1] / sum(restecg) * 100,restecg[2] / sum(restecg) * 100]

# exang = data[data['HeartDisease'] == 1]['ExerciseAngina'].value_counts()
# exang = [exang[0] / sum(exang) * 100,exang[1] / sum(exang) * 100]

# slope = data[data['HeartDisease'] == 1]['ST_Slope'].value_counts()
# slope = [slope[0] / sum(slope) * 100,slope[1] / sum(slope) * 100,slope[2] / sum(slope) * 100]

# fig, ax = plt.subplots(nrows = 3,ncols = 2,figsize = (15,15))

# plt.subplot(3,2,1)
# plt.pie(sex,labels = ['Male','Female'],autopct='%1.1f%%',startangle = 90,explode = (0.1,0),colors = colors,
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('Sex')

# plt.subplot(3,2,2)
# plt.pie(cp,labels = ['ASY', 'NAP', 'ATA', 'TA'],autopct='%1.1f%%',startangle = 90,explode = (0,0.1,0.1,0.1),
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('ChestPainType')

# plt.subplot(3,2,3)
# plt.pie(fbs,labels = ['FBS < 120 mg/dl','FBS > 120 mg/dl'],autopct='%1.1f%%',startangle = 90,explode = (0.1,0),colors = colors,
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('FastingBS')

# plt.subplot(3,2,4)
# plt.pie(restecg,labels = ['Normal','ST','LVH'],autopct='%1.1f%%',startangle = 90,explode = (0,0.1,0.1),
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('RestingECG')

# plt.subplot(3,2,5)
# plt.pie(exang,labels = ['Angina','No Angina'],autopct='%1.1f%%',startangle = 90,explode = (0.1,0),colors = colors,
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('ExerciseAngina')

# plt.subplot(3,2,6)
# plt.pie(slope,labels = ['Flat','Up','Down'],autopct='%1.1f%%',startangle = 90,explode = (0,0.1,0.1),
#         wedgeprops = {'edgecolor' : 'black','linewidth': 1,'antialiased' : True})
# plt.title('ST_Slope')

# plt.show()

# Numerical Features vs Target Variable (HeartDisease)

# fig, ax = plt.subplots(nrows = 5,ncols = 1,figsize = (15,30))
# for i in range(len(numerical_features)):
#     plt.subplot(5,1,i+1)
#     sns.countplot(x= numerical_features[i],data = data,hue = "HeartDisease",palette = colors, edgecolor = 'black')
#     title = numerical_features[i] + ' vs Heart Disease'
#     plt.legend(['No Heart Disease','Heart Disease'])
#     plt.title(title)

# data['RestingBP_Group'] = [ int(i / 5) for i in data['RestingBP']]
# data['Cholesterol_Group'] = [ int(i / 10) for i in data['Cholesterol']]
# data['MaxHR_Group'] = [ int(i / 5) for i in data['MaxHR']]
# data['Oldpeak_Group'] = [ int( (i*10) / 5) for i in data['Oldpeak']]

# fig, ax = plt.subplots(nrows = 4,ncols = 1,figsize = (10,25))
# group_numerical_features = [i + '_Group' for i in numerical_features[1:]]
# for i in range(len(group_numerical_features)):
#     plt.subplot(4,1,i+1)
#     sns.countplot(x= group_numerical_features[i],data = data,hue = "HeartDisease",palette = colors, edgecolor = 'black')
#     plt.legend(['No Heart Disease', 'Heart Disease'])
#     title = group_numerical_features[i] + ' vs Heart Disease'
#     plt.title(title)

# Numerical features vs Categorical features w.r.t Target variable(HeartDisease)

fig,ax = plt.subplots(nrows = 1,ncols = 3,figsize = (15,5))
for i in range(3):
    plt.subplot(1,3,i+1)
    sns.stripplot(x = 'Sex',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors);
    plt.legend(['No Heart Disease', 'Heart Disease'])
    title = numerical_features[i] + ' vs Sex' 
    plt.title(title)

fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (15,5))
for i in [-1,-2]:
    plt.subplot(1,2,-i)
    sns.stripplot(x = 'Sex',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors);
    plt.legend(['No Heart Disease', 'Heart Disease'])
    title = numerical_features[i] + ' vs Sex' 
    plt.title(title)

# # plt.show()

# ChestPainType vs Numerical Features
fig,ax = plt.subplots(nrows = 1,ncols = 3,figsize = (15,5))
for i in range(3):
    plt.subplot(1,3,i+1)
    sns.stripplot(x = 'ChestPainType',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors);
    plt.legend(['No Heart Disease', 'Heart Disease'])
    title = numerical_features[i] + ' vs ChestPainType'
    plt.title(title)

fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (15,5))
for i in [-1,-2]:
    plt.subplot(1,2,-i)
    sns.stripplot(x = 'ChestPainType',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors);
    plt.legend(['No Heart Disease', 'Heart Disease'])
    title = numerical_features[i] + ' vs ChestPainType' 
    plt.title(title)

# # plt.show()

# # FastingBS vs Numerical features

# fig,ax = plt.subplots(nrows = 1,ncols = 3,figsize = (15,5))
# for i in range(3):
#     plt.subplot(1,3,i+1)
#     sns.stripplot(x = 'FastingBS',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors);
#     plt.legend(['No Heart Disease', 'Heart Disease'])
#     title = numerical_features[i] + ' vs Fasting Blood Sugar' 
#     plt.title(title)

# fig,ax = plt.subplots(nrows = 1,ncols = 2,figsize = (15,5))
# for i in [-1,-2]:
#     plt.subplot(1,2,-i)
#     sns.stripplot(x = 'FastingBS',y = numerical_features[i],data = data,hue = 'HeartDisease',palette = colors)
#     plt.legend(['No Heart Disease', 'Heart Disease'])
#     title = numerical_features[i] + ' vs Fasting Blood Sugar' 
#     plt.title(title)

# # plt.show()

# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import chi2
# features = df1.loc[:,categorical_features[:-1]]
# target = df1.loc[:,categorical_features[-1]]

# best_features = SelectKBest(score_func = chi2,k = 'all')
# fit = best_features.fit(features,target)

# print(fit.scores_)

# featureScores = pd.DataFrame(data = fit.scores_,index = list(features.columns),columns = ['Chi Squared Score']) 

# plt.subplots(figsize = (5,5))
# sns.heatmap(featureScores.sort_values(ascending = False,by = 'Chi Squared Score'),annot = True,cmap = colors,linewidths = 0.4,linecolor = 'black',fmt = '.2f')
# plt.title('Selection of Categorical Features')

plt.tight_layout()
plt.show()
