
# coding: utf-8

# In[ ]:


bag = [1,2,3,4,5,6]
for i, e in enumerate(bag):
    print(i, e)


# In[4]:


a = 1
b = 2
a,b = b,a
print(a, b)


# In[7]:


bag = [[0] for _ in range(5)]
print(bag)
bag[0][0] = 1
print(bag)


# In[8]:


name = "daixiong"
age = 22
born_in = "hubei"
string = "myname is {0} and I'm {1}. I was born in {2}.".format(name, age, born_in)
print(string)


# In[9]:


def binary():
    return 0, 1
zero, one = binary()
print(zero, one)


# In[13]:


countr = {}
bag = [1,2,3,23,2,3,2,3,24,2,4,2,4,2,4]
for i in bag:
    countr[i] = countr.get(i, 0) + 1
for i in range(100):
    print("Count of {}: {}".format(i, countr.get(i, 0)) )


# In[14]:


from collections import Counter
bag = [2,3,4,23,4,234,2,4,24,2,42,4,24]
countr = Counter(bag)

for i in range(100):
    print("Count of {}: {}".format(i, countr[i]))


# In[19]:


bag = [1,2,3,2,3,23,1,4,1,42354,36,54,645,7,5467,54]
a = bag.list[::-10]
print(a)


# In[25]:


def cache(func):
    data = {}
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)}'
        if key in data:
            result = data.get(key)
            print('cache')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result
    return wrapper

@cache
def rectangle_area(length, width):
    return length*width

rectangle_area(2, 3)
rectangle_area(2, 3)
        


# In[5]:


r1 = {'name': 'daixiong', 'age': 24 , 'salary': 5000}
r2 = {'name': 'daixiong', 'age': 24 , 'salary': 4000}
r3 = {'name': 'daixiong', 'age': 24 , 'salary': 2000}
a = [r1, r2, r3]
for i in range(len(a)):
    
    print(a[i])

