#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv("C://Users\student\Desktop\E2 SEM2\DSP\insurance_data.csv")
df.head()


# In[4]:


plt.scatter(df.age,df.bought_insurance,marker='+',color='blue')
plt.show()


# In[12]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance,train_size=0.3)


# In[16]:


from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
y_predicted=model.predict(x_test)
print(model.predict_proba(x_test))
print(model.score(x_test,y_test))
print("y_predicted:",y_predicted)
print("coefficient:",model.coef_)
print("Model intercept:",model.intercept_)


# In[20]:


#sea born
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5])
plt.show()


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5],hist=False)
plt.show()


# In[ ]:




