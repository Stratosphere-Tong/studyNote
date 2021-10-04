# MATLAB语法
## 基础命令
### edit filename
作用：编辑filename代码，若不存在该文件，自动创建一个。
### clear
作用：删除变量
用法：
```
clear num1;//删除变量num1
clear;//删除所有变量
```
### clc
作用：清屏
### who、whos
作用：查看当前我们所有的变量
### 注释符号
%
### help filename
输出file的所有注释，可以查看函数用法
### 强制类型转换
```
baseNum=123.456;
toUint32=uint32(baseNum);
```
## 常用函数
#### disp(elem)
作用：输出变量elem
#### sprintf()
作用：格式化字符串
用法：
```MATLAB
sentence='hello world!';
new_sentence=sprintf('hxt says:%s \n',sentence);
```
#### fprintf()
作用：等效于disp(sprintf())
#### roots()
作用：求解一元二次方程的根
参数：一个存储了二次项系数，一次项系数和常数项的数组
用法：
```MATLAB
p=[1 -1 -1];
r=roots(p)
```
#### solve()
作用：求解函数结果
#### ezplot()
作用：绘制函数图像
参数：ezplot(func,left,right)
#### fzero()
作用：返回函数零点
参数：fzero(func,num)
返回num附近的函数func的零点
#### zeros(m,n);
作用：返回一个m行n列的矩阵 
<font color=red>注：matlab的矩阵以1为起始下标</font>
#### plot(x,y,char)
作用：在（x,y）点标注char
## 函数形式
```
function 返回值 = filename(参数)
%功能：
%参数：
%返回值：
函数体
return
```

#### for循环
```MATLAB
for k=1:n
    f(k)=f(k-1)+f(k-2);
end
% for循环1和n都能取到
```
for 循环的实质是对于一个矩阵，对每一列进行一次循环
如：
```MATLAB
for n=[1 2 3;4 5 6;7 8 9]
   n
end
```
将返回 
      n=[1;4;7]
      n=[2;5;8]
      n=[3;6;9]

#### 矩阵运算
用法：行用';'分隔，列用' '分隔。

A=[1 2 3;
   4 5 6;
   7 8 9];
B=[1 1 1;
   1 1 1;
   1 1 1];
<font color=red>
A/B==A*1/B==A*inv(B)  右除
A\B==1/A*B==inv(A)*B  左除
巧记：斜杠往哪边靠，哪个矩阵是逆矩阵
</font>

【点运算符】
A.*B表示A和B中的每一个对应元素相乘
./ .^同理
~=不等于
#### 积分
```MATLAB
syms x;
f=sin(x);
F1=int(f,x);%不定积分
F2=int(f,x,0,1)%定积分
```

### 求解多项式
1. 已知系数——poly2sym()
   ```MATLAB
   p=[1 2 3];
   y=poly2sym(p);
   disp(y);
   ```
   输出 y==x^2+2*x+3
2. 已知根——poly()
   ```MATLAB
   x=[1 2];
   p=poly(x);%返回该多项式的系数
   y=poly2sym(p);%得到多项式
   ```

### 取模运算
fix()截尾取整
round()四舍五入取整
floor()向下取整
ceil()向上取整

mod()取模
rem()取余
## 矩阵高级处理
#### 特殊矩阵
zeros 零矩阵
ones 1矩阵
eye 单位矩阵

## 图形绘制

### 绘制图像
```MATLAB
plot(x,y,option);
fplot(funcx,funcy,[xmin,xmax],option); 
fplot(@(x)sin(x),[0,pi],'bs');
%若希望绘制一个共用x的图像
plot(x,[sin(x);sin(2*x);sin(3*x)]);
```
### 图形标注
```MATLAB
title(图形标题，属性名，属性值)
xlabel(x轴说明)
text(x,y,说明)
legend(图例1，图例2，...)
```
### 坐标控制
```MATLAB
axis([xmin,xmax,ymin,ymax,zmin,amax])
% axis的其他用法
axis equal: 横纵坐标采用等长刻度
axis square: 产生正方形坐标系
axis auto: 使用默认设置
axis off: 取消坐标轴
axis on: 显示坐标轴
```
### 给坐标加网格
```MATLAB
grid on
grid off
% 给坐标加边框
box on 
box off
```
### 保持图形(若不保持，则每次plot会刷新图像)
```MATLAB
hold on
hold off
hold
```
### 分割图形(将一个背景板分割成子图)
```MATLAB
subplot(m,n,p)
%% 表示将背景板分割成mxn的分割，现在对第p号区进行绘制
```
### 其他坐标系下的二维曲线图
1. 对数坐标图
```MATLAB
semilogx(x1,y1,选项1,x2,y2,选项2,...);
semilogy(...);
loglog(...);
```
1. 极坐标图
```MATLAB
polar(theta,rho,选项)
```
### 统计图
建议自行百度

## 数据统计分析



## 经典代码
3. 求水仙花数
当一个数的每一位数的立方之和等于原数称为水仙花数
```MATLAB
data=100:999;
x1=rem(data,10);
x2=rem(fix(data/10),10);
x3=fix(x/100);

ind=find(data==x1.^3+x2.^3+x3.^3); %find函数和.^的运用
disp(data(ind));
```
2. 使用蒙特卡洛方法求解圆周率
```MATLAB
s=0;
n=10000000;
for n=1:n
   x=rand(1);
   y=rand(1);
   if x*x+y*y<1
      s=s+1;
   end
end
pai=4*s/n
```
3. 带图例绘制sinx sin2x sin3x 函数图像
```MATLAB
x=linspace(0,2*pi,100);
plot(x,[sin(x);sin(2*x);sin(0.5*x)]);% 每一行对应一个函数
axis([0,7,-1.2,1.2]);
title('不同频率正弦函数图像');
xlabel('Variable X');ylabel('Variable Y');
text(2.5,sin(2.5),'sin(x)');
text(1.5,sin(2*1.5),'sin(2x)');
text(5.5,sin(0.5*5.5),'sin(0.5*x)');
legend('sin(x)','sin(2x)','sin(0.5x)');
grid on
box on
```
4. 图形窗口的分割
```MATLAB
x=linspace(0,2*pi,100);
subplot(2,2,1);
plot(x,sin(x)-1);
title('sin(x)-1');
subplot(2,1,2);
plot(x,tan(x));
title('tan(x)');
subplot(4,4,3);
plot(x,cos(x)+1);axis([0,2*pi,0,2]);
title('cos(x)-1');
grid on
```