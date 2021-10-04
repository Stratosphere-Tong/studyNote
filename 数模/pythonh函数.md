# 数据分析
## matplotlib
### plot()——最基础的绘图函数
```Python
import numpy as np
import matplotlib.pyplot as plt

x=linspace(0.5,3.5,300)#在0.5 和3.5之间均匀的取300个数
y=np.sin(x)

plt.plot(x,y,color='blue',linetyle='-',linewidth=1,marker='o',markersize=4,label='Line')#参数建议百度
```
### plot()其他属性设置
```Python
plt.xlim(1,3)
plt.ylim(min(y),max(y))
plt.xticks([...],[...])#将替换的x坐标变成...

plt.ylabel('value')
plt.title('')#标题
# 图例显示
# loc--位置（1：右上，2：左上，3：左下，4：右下）
plt.legend(loc=1)
#网格线
plt.grid(axis='x')# gird(axis='both')也可以
plt.grid(axis='y')
#保存图片
plt.savefig('plot.png',dpi=800)
#显示图片
plt.show()
```
### 基本元素
1. Figure：画布
2. Axes：子图

示例：
```Python
#fig,ax=plt.subplots(figsize(14,7)) 不设置子图
fig,ax=plt.subplots(1,2,figsize(14,7))# 设置宽为1，长为2 的子图
#通过类似数组的方式对子图进行操作
ax[0].plot(x,y)
ax[1].plot(x,z)

```
### scatter()函数——寻找变量之间的关系
#### 定义
scatter(x,y,s=10,c='b',marker='+',cmap=None,label='scatter')
s:点的大小
c:点的颜色
marker:点的样式
cmap:颜色图
label:标签
plt.colorBar():生成一个表示程度的柱状图 可以清晰的看出不同颜色代表的意思
set_label()为该对象设置一个标签
#### 示例代码——生成热力图
```Python
import pandas as pd
import matplotlib.pyplot as plt

url='C:\\Users\\hxt\\Desktop\\数模杉树杯\\第四问\\orders.xlsx'
df=pd.read_excel(url)
x=df.loc[0]
y=df.loc[1]
orders=df.loc[2]

ax=plt.scatter(x.values[1:],y.values[1:],c=orders.values[1:])
cbar=plt.colorbar()
cbar.set_label('Ratio')
plt.savefig('plot.png',dpi=800)
plt.title("散点图")
plt.show()

```
### bar()函数&barth函数——垂直&水平柱状图
#### 定义
bar(x,y,align='center',color='c'...)
### hist()函数——直方图
### seaborn.distplot()函数——直方图+拟合曲线
### pie()——饼状图

## numpy
### 生成ndarray
```Python
import numpy as np
data1=[1,2,3]
data2=[4,5,6]
arr=np.array(data1,data2)
arr.shape()#检查矩阵的大小

#生成特殊矩阵
np.zeros((m,n))
np.ones((m,n))
np.empty((x,y,z,...))
```
### 基础切片
```Python
arr=np.arange(10)
#arr=[0,1,2,3,4,5,6,7,8,9]
arr[5:7]=12#返回的是地址，修改会影响原数组
# arr=[0,1,2,3,4,5,12,12,8,9]
tmp=arr[5:7].copy()#显式的拷贝才不会影响
tmp=12
# arr=[0,1,2,3,4,5,6,7,8,9]

#二维数组的切片
print(arr[2:,1:])
```
## pandas
更多操作见 https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
### describe()函数
返回datafram的各种信息，在数模中相当有用
### pd.Datafram()
1. 创建方式1(可定义行列的名字)
```Python
df = pd.DataFrame([['a', 'man', 120, 90],
                   ['b', 'woman', 130, 100],
                   ['a', 'man', 110, 108],
                   ['a', 'woman', 120, 118]], columns=['level', 'gender', 'math','chinese'])
```