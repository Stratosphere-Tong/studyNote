# Top 50 matplotlib Visualizations
## Set up
```Python
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

# Version
print(mpl.__version__)  #> 3.0.0
print(sns.__version__)  #> 0.9.0
```

## Correlation
The plots under correlation is used to visualize the relationship between 2 or more variables. That is, how does one variable change with respect to another.
用于表示不同变量之间的相关性。
### Scatter
关键步骤：
1. 对不同的种类给予不同的颜色
```Python
colors= [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
```
2. 绘制图像的操作方法(loc iloc函数的操作方法)
```Python
for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', 
                data=midwest.loc[midwest.category==category, :], 
                s=20, c=colors[i], label=str(category))
```
<font color=red>其中参数如果传递data，则最开始两个字符串代表data的两个columns，否则直接传递x,y向量</font>

3. 设置标签
```Python
ax.set(title='...',xlabel='....',ylabel='.....')
```
4. x,y轴附带频率直方图关键代码
```Python
ax_bottom.hist(df.displ, 40, histtype='stepfilled', orientation='vertical', color='deeppink')
ax_bottom.invert_yaxis()

# histogram in the bottom
ax_right.hist(df.hwy, 40, histtype='stepfilled', orientation='horizontal', color='deeppink')

``` 
1. 示例代码
+ `按照颜色不同分别代表不同类型的变量示例代码`
```Python
# Import dataset 
midwest = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

# Prepare Data 
# Create as many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, category in enumerate(categories):
    plt.scatter('area', 'poptotal', 
                data=midwest.loc[midwest.category==category, :], 
                s=20, c=colors[i], label=str(category))

# Decorations
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
plt.legend(fontsize=12)    
plt.show()    
```
![2]

+ `Marginal Histogram 单个变量的频率直方图`
```Python
# Import Data
df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")

# Create Fig and gridspec
fig = plt.figure(figsize=(16, 10), dpi= 80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

# Define the axes
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# Scatterplot on main ax
ax_main.scatter('displ', 'hwy', s=df.cty*4, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df, cmap="tab10", edgecolors='gray', linewidths=.5)

# histogram on the right
ax_bottom.hist(df.displ, 40, histtype='stepfilled', orientation='vertical', color='deeppink')
ax_bottom.invert_yaxis()

# histogram in the bottom
ax_right.hist(df.hwy, 40, histtype='stepfilled', orientation='horizontal', color='deeppink')

# Decorations
ax_main.set(title='Scatterplot with Histograms \n displ vs hwy', xlabel='displ', ylabel='hwy')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

xlabels = ax_main.get_xticks().tolist()
ax_main.set_xticklabels(xlabels)
plt.show()
```
![3]
### 箱线图 Marginal Boxplot
有助于确定 X,Y 轴的中位数，25%和75%的百分位数

关键代码
```Python
# Define the axes
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# Scatterplot on main ax
ax_main.scatter('displ', 'hwy', s=df.cty*5, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df, cmap="Set1", edgecolors='black', linewidths=.5)

# Add a graph in each part 绘制箱线图的参数
sns.boxplot(df.hwy, ax=ax_right, orient="v")
sns.boxplot(df.displ, ax=ax_bottom, orient="h")
```
![4]
## Correllogram 不同变量之间相关性
### heatmap
```Python
sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0, annot=True)
```
df.corr()表示返回一个矩阵表示不同变量之间的相关系数
使用heatmap可视化效果很好
![5]
## Pairwise Plot
研究不同变量之间的相关性
```Python
方法：sns.pairplot(data,kind=...,reg_kind=...,hue=....,x_vars=['...'],y_vars=['....'])
```
kind='reg' or 'scatter': 选择不同变量之间的关系表示图
reg_kind='hist' or 'kde':选择单个变量的关系表现图
hue='种类'：图片中不同种类给予不同颜色
x_vars=[]: 主动选择研究的变量
![6]
## Diverging Bars 发散条形图
用于研究同一指标不同种类的可视化图形
其在所有数据上都减掉了整体数据的均值，这样大于均值的数据依然为正，而低于均值的数据就会变成负数

> 若希望给图像上标注对应的数字可用如下代码,使用text()函数
```Python
for x,y,tex in zip(df.x,df.index,df.x):
    plt.text(x,y,round(tex,2),size=8,horizontalalignment='right' if x < 0 else 'left', 
                 verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':14}))
```

#### 示例代码：
```Python
# Prepare Data
df = pd.read_csv("https://github.com/selva86/datasets/raw/master/mtcars.csv")
x = df.loc[:, ['mpg']]
df['mpg_z'] = (x - x.mean())/x.std()
df['colors'] = ['red' if x < 0 else 'green' for x in df['mpg_z']]
df.sort_values('mpg_z', inplace=True)
df.reset_index(inplace=True)

# Draw plot
plt.figure(figsize=(14,10), dpi= 80)
plt.hlines(y=df.index, xmin=0, xmax=df.mpg_z, color=df.colors, alpha=0.4, linewidth=5)
# 注意这里先用的是index 不能直接使用df.cars 否则会直接将cars当作坐标来带入
# Decorations
plt.gca().set(ylabel='$Model$', xlabel='$Mileage$')
#这里将index 替换为df.cars
plt.yticks(df.index, df.cars, fontsize=12)
plt.title('Diverging Bars of Car Mileage', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.show()

```
![7]

##  








[2]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/1_Scatterplot_Matplotlib-min.png?ezimgfmt=ng:webp/ngcb4
[3]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/6_Marginal_histogram_Matplotlib-min.png
[4]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/7_Marginal_boxplot_Matplotlib-min.png?ezimgfmt=ng:webp/ngcb4
[5]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/8_Correlogram_Matplotlib-min.png?ezimgfmt=ng:webp/ngcb4
[6]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/9_Pairplot_lines_Seaborn-min.png?ezimgfmt=ng:webp/ngcb4
[7]: https://www.machinelearningplus.com/wp-content/uploads/2018/11/10_Diverging_bars_Matplotlib-min.png?ezimgfmt=ng:webp/ngcb4