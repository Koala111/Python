
# coding: utf-8

# In[8]:


# 基本属性
import numpy as np

array = np.array([
    [1, 2, 3],
    [2, 3, 4]
])

print(array) # 打印出矩阵
print('number of dim:', array.ndim) # 维数
print('shape:', array.shape)
print('size:', array.size)


# In[33]:


import numpy as np

a = np.array([[1, 32, 3],
              [2, 34, 23]])
b = np.zeros((3, 4))
c = np.ones((3, 5))
d = np.arange(12).reshape((3, 4))
e = np.linspace(1, 10, 6).reshape((2, 3))

print(a)
print(b)
print(c)
print(e)


# In[12]:


# 基本运算
import numpy as np

a = np.array([[1, 1],
            [0, 1]])
b = np.arange(4).reshape(2, 2)
x = np.random.random((2, 4))
d = 10*np.sin(a)
e = 10*np.cos(a)
f = 10*np.tan(a)

c = a*b
c_dot = np.dot(a, b)
print(c_dot)
print(c)
print(np.max(x))


# In[21]:


import numpy as np
A = np.arange(2, 14).reshape((3, 4))

print(np.argmin(A)) # 最小值索引
print(np.argmax(A)) # 最大值索引
print(np.mean(A, axis = 0)) # 平均值
print(np.average(A)) # 平均值索引
print(np.median(A)) # 中位数索引
print(np.cumsum(A)) # 累加
print(np.diff(A)) # 累差
print(np.nonzero(A)) # 索引
print(np.sort(A)) # 排序
print(np.transpose(A)) # 翻转
print(np.clip(A, 5, 9)) # 所有小于5的都等于5， 大于9的都等于9
print(A)


# In[38]:


# 索引
import numpy as np

A = np.arange(3, 15).reshape(3, 4)
print(A)
print(A[2][2]) # 索引
print(A[2, 2])
print(A[2,:])
print(A[:, 1])
print(A[1, 1:3])

for row in A:
    print(row)
    
for column in A.T: # 对A翻转
    print(column)
print(A.flatten()) # 返回它的序列   
for item in A.flat:
    print(item)
    


# In[49]:


# 数组合并
import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A, B)) # vertical stack
D = np.hstack((A[:,np.newaxis], B[:,np.newaxis]))
E = np.concatenate((A, B, B, A), axis = 0)
print(A.shape, C.shape) # horizontal stack
print(D)
print(E)


# In[55]:


# 分割
import numpy as np

A = np.arange(12).reshape((3, 4))

print(A)
print(np.split(A, 3, axis = 0)) # 1 代表对列进行操作，0 代表对行进行操作
print(np.array_split(A, 3, axis = 1)) # 不等项的分割
print(np.vsplit(A, 3))
print(np.hsplit(A, 2))


# In[61]:


# 赋值
import numpy as np
a = np.arange(4)
b = a.copy() # deep copy
c = a
d = b
print(a)
a[0] = 11
print(a)
print(b)
print(b is a)


# In[77]:


# panda
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 44, 1])
dates = pd.date_range('20181009', periods = 6)
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = ['a', 'b', 'c', 'd'])
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
                    
print(s)
print(dates)
print(df)
print(df1)
print(df2)
print(df2.dtypes) # 类型
print(df2.index) # 序号
print(df2.columns)
print(df2.values)
print(df2.describe()) # 数据形式的
print(df2.T) # 转换
print(df2.sort_index(axis = 0, ascending = False)) # 倒序
print(df2.sort_values(by = 'E')) # value sort


# In[88]:


# 选择数据 标签，取值范围
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

print(dates)
print(df)
print(df['A'], df.A)
print(df[0:3])
print(df['20130102':'20130104'])

# select by label:loc
print(df.loc['20130102'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20130102', ['A', 'B']])

# select  by position :iloc
print(df.iloc[3:5, 1:3])

# mixed selection :ix
# print(df.ix[:3, ['A', 'C']])
print(df[df.A > 8])


# In[95]:


# 设置值
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

df.iloc[2, 2] = 1111
df.loc['20130101', 'B'] = 2222
df.A[df.A > 4] = 0
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101',periods=6)) 
print(df)


# In[107]:


# pandas 处理丢失数据
import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0, 1] = np.nan
df.iloc[0, 2] = np.nan

print(df)
# print(np.any(df.isnull() == True)
print(df.dropna(axis = 0, how = 'any'))

print(df.fillna(value = 0))


# In[110]:


import pandas as pd #加载模块

#读取csv
data = pd.read_csv('c:/student.csv')

#打印出data
print(data)
# data.to_pickle('student.pickle')


# In[121]:


# 合并多个date
import pandas as pd
import numpy as np

# concatenating
'''
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])
res = pd.concat([df1, df2, df3], axis = 0, ignore_index = True)
print(df1)
print(res)

# join
#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

#纵向"外"合并df1与df2
res = pd.concat([df1, df2], axis=0, join='inner', ignore_index = True)

print(df1)
print(df2)
print(res)

#定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

#纵向"外"合并df1与df2
res = pd.concat([df1, df2], axis=0, join='outer')

print(res)
'''
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])

#将df2合并到df1的下面，以及重置index，并打印出结果
res = df1.append(df2, ignore_index=True)
print(df1)
print(df2)
print(res)


# In[135]:


# merge 合并
import pandas as pd
'''
#定义资料集并打印出
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                             'A': ['A0', 'A1', 'A2', 'A3'],
                             'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                              'C': ['C0', 'C1', 'C2', 'C3'],
                              'D': ['D0', 'D1', 'D2', 'D3']})
res = pd.merge(left, right, on = 'key')
print(left)
print('*'*20)
print(right)
print(res)

#定义资料集并打印出
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                      'key2': ['K0', 'K1', 'K0', 'K1'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                       'key2': ['K0', 'K0', 'K0', 'K0'],
                       'C': ['C0', 'C1', 'C2', 'C3'],
                       'D': ['D0', 'D1', 'D2', 'D3']})
# how = left, right, outer, inner
res = pd.merge(left, right, on = ['key1', 'key2'], how = 'outer')
print(left)
print(right)
print(res)

#定义资料集并打印出
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})

print(df1)
res = pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column')
print(res)
'''
#定义资料集并打印出
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)
res = pd.merge(left, right, left_index=True, right_index=True, how='inner')
print(res)

#定义资料集
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})

#使用suffixes解决overlapping的问题
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(res)


# In[146]:


# plot 图表
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# series
data = pd.Series(np.random.randn(1000), index = np.arange(1000))
data = data.cumsum()

# DataFrame
data = pd.DataFrame(np.random.randn(1000, 4),
                   index = np.arange(1000),
                   columns = list("ABCD"))
data = data.cumsum()
print(data.head())
# data.plot()
# plot method: 'bar', 'hist' , 'box'
ax = data.plot.scatter(x='A',y='B',color='DarkBlue',label='Class1')
# 将之下这个 data 画在上一个 ax 上面
data.plot.scatter(x='A',y='C',color='LightGreen',label='Class2',ax=ax)
plt.show()

