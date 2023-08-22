#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
data_frame = pd.read_excel(r"C:\Users\HariK\OneDrive\Desktop\sample.xlsx")
data_frame.head()


# In[5]:


data_frame.info()


# In[7]:


data_frame.describe()


# In[8]:


#Top 10 Unicorn Companies In the World based on Valuation:
import pandas as pd
file = pd.read_csv(r"C:\Users\HariK\Downloads\unicorn\unicorn_startup_companies.csv")
file[['Company','Valuation ($B)','Country','Industry']].head(10)


# In[10]:


characters = input()
characters1 = list(set(characters))
characters1.sort()
result = ""
for i in range(len(characters1)):
    each_char = characters.count(characters1[i])
    result += str(each_char) + characters1[i]
    
print(result)


# In[ ]:




