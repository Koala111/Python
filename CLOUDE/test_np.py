import numpy as np
'''
data=np.array([1,2,3,4,5])


print(data.ndim) #输出维度    
print(data.shape)        #输出几列 

data=np.zeros(10) #输出全0的一行

data=np.ones(10)

data=np.ones((10,10))

data=np.arange(10)
print(data[5])
print(data[3:6]) #切片到5，切片得到的数据对应的还是原始数据，任何修改才会反映到原始数据上的
data[3:6].copy() #拷贝副本
print(data.reshape((2,5))) #折一下
print(data.reshape((2,5)).T) #矩阵的转置
np.sqrt(data) #求平方根
data=np.array(              #二维数组
        [
            [1,2,3],
            [4,5,6]            
        ]     
             ) 
print(data[0][1])
print(data[0,1])
'''