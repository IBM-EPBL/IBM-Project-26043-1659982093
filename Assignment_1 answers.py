#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1
s = "Hi there Sam!"
str=s.split(" ")
for x in str:
    print(x)


# In[3]:


#2
planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));


# In[4]:


#3
d = {'k1':
     [1,
      2,
      3,
      {'tricky':
       ['oh',
        'man',
        'inception',
        {'target':
         [1,
          2,
          3,
          'hello'
         ]
        }
       ]
      }
     ]
    }

print(d['k1'][3]["tricky"][3]['target'][3])


# In[6]:


#4.1
import numpy as np
custom1=np.zeros(10)
print(custom1)

#4.2
custom2=np.ones(10)*5
print(custom2)


# In[7]:


#5
array=np.arange(20,36,2)
print(array)


# In[8]:


#6
np.arange(0,9).reshape((3,3))


# In[9]:


#7
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))


# In[15]:


#8
matrix =np.random.randint(10, size=(3,2))
print(matrix)


# In[16]:


#9
import pandas as pd
res= pd.date_range(start ='1-1-2023', 
         end ='1-2-2023')
for val in res:
    print(val)


# In[17]:


#10
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

df = pd.DataFrame(lists, columns =['A','B','C']) 
print(df)


# In[ ]:




