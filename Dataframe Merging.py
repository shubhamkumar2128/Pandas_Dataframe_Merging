#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd

df_temp=pd.DataFrame({
    "city":["Delhi","UP","MP","Kolkata","Tamilnadu"],
    "temprature":[28,23,27,29,26]
})
print(df_temp)


# In[36]:


df_hum=pd.DataFrame({
    "city":["Delhi","UP","MP","Kolkata"],
    "humidity":[45,50,54,34]
})
print(df_hum)


# In[68]:


#Merge two dataframe(outer join)
merge=pd.merge(df_temp,df_hum,how="outer",indicator=True,on="city")
print(merge)


# In[69]:


#Merge two dataframe(left join)
merge=pd.merge(df_temp,df_hum,how="right",indicator=True,on="city")
print(merge)


# In[70]:


#(intersection join)
merge=pd.merge(df_temp,df_hum,indicator=True,on="city")
print(merge)


# In[71]:


#(left join)
merge=pd.merge(df_temp,df_hum,how="left",indicator=True)
print(merge)


# In[62]:


df1=pd.DataFrame({
    "city":["Delhi","UP","MP","Kolkata"],
    "humidity":[45,43,55,34],
    "temprature":[28,23,27,26]
})
print(df1)


# In[63]:


df2=pd.DataFrame({
    "city":["Delhi","UP","MP"],
    "temprature":[28,23,27],
    "humidity":[45,43,55]
})
print(df2)


# In[77]:


#when two dataframe has same column name
m2=pd.merge(df1,df2,on="city")
print(m2)


# In[79]:


#Explicit suffix
m2=pd.merge(df1,df2,on="city",suffixes=("_left","_right"))
print(m2)

