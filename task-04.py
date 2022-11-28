#!/usr/bin/env python
# coding: utf-8

# In[ ]:


############### TASK NO:04 BASIC COMMANDS AND FUNCTIONS OF NUMPY#################


# In[12]:


# Task 4-a
import numpy as np
a=np.zeros(5)
b=np.zeros((5, 4))
c=np.zeros((5, 4, 3))
print('a=',a)
print('b=',b)
print('c=',c)


# In[23]:


# task 4-b
import numpy as np
data=[1.2, 2.2, 3.2, 4.2, 5.2]
a=np.array(data)
print('a=', a)
print('a*a=', a*a)
print('a-a=', a-a)
print('1/a=', 1/a)
print('a*0.5=', a*0.5)
b=a[2:4] # slicing
print('sliced array:', b)
b[1]=2
print ('new b:', b)
b[:]=44 #all numbers changed in the sliced part
print('latest b:',b)
print('updated a:', a) # as sliced part was from a so the data enteries of that sliced part also changed in a rest of the 
                    # enteries remained same


# In[40]:


# task 4-c
import numpy as np
a = np.arange(10)
print('a=',a)
print('in between elements 2-7:', a[2:7])
print('in between 7 and 9:', a[-3:-1])
print('with 2 increment:', a[0:9:2])


# In[44]:


# task 4-d
b=[[1,2,3], [4,5,6],[7,8,9]]
c=np.array(b)
print('my matrix:' ,c)
print ('row wise decrement:',c[:2])
print('row and column wise:', c[:2,1:])


# In[48]:


#task 4-e
a=np .arange(9)
b=a.reshape((3,3))
print('my matrix:', b)
print("transpose=", b.T)
print (np.dot(b.T, b))
print (np.dot(b, b.T))
print('square root:', np.sqrt(b))
print('exponential:', np.exp(b))


# In[56]:


from numpy import random
x=np.random.randn(4)
y=np.random.randn(4)
print('x=',x)
print('y=',y)
print('x+y=', np.add(x,y))
a=np.random.randn(2,5)
print(' mean of a:', a.mean)
print('mean of a:', np.mean(a))


# In[62]:


a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)
print(b)
print ('column wise mean:',b.mean(axis=0))
print('row wise mean:', b.mean(axis=1))
print(b.sum(0)) # coulum wise normal sum
print(b.cumsum(1)) # row wise cummulative sum


# In[ ]:




