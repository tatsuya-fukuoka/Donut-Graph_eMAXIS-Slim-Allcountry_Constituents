import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('vt.csv')

label = df['Country'].values.tolist()

fig = plt.figure()
plt.title('<対象インデックスの国・地域別構成比率>')
plt.text(-1.2,-1.2,'ｅＭＡＸＩＳ Ｓｌｉｍ 全世界株式（オール・カントリー）,2022.2.28',size =7)
plt.rcParams['font.sans-serif'] = 'MS Gothic' 
# 円グラフ (外側)
x1 = df['Rate'].values
plt.pie(x1, labels=label, counterclock=False, autopct="%.1f",pctdistance=0.9,startangle=90,labeldistance=1.0,rotatelabels=True)

# 円グラフ (内側, 半径 70% で描画)
rate = [i for i in range(0,len(label)) if label[i] == 'その他']
num1 = np.array([float(x1[i]) for i in range(0,rate[0]+1)]).sum()
num2 = np.array([float(x1[i]) for i in range(rate[0]+1,rate[1]+1)]).sum()

x2 = np.array([num1, num2])
label2 = ['先進国','新興国']
colors = ["orange", "gray"]
plt.pie(x2, labels=label2, counterclock=False, startangle=90, radius=0.7,labeldistance=0.8,wedgeprops={'linewidth': 3, 'edgecolor':"white"},colors=colors)
 
# 中心 (0,0) に 40% の大きさで円を描画
centre_circle = plt.Circle((0,0),0.4,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

#plt.show()
fig.savefig('対象インデックスの国_地域別構成比率.png')