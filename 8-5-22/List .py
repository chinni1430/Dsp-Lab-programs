#!/usr/bin/env python
# coding: utf-8

# In[1]:


#printing list
L=[1,2,3,4]
print(L)


# In[1]:


L1=[]
L1.extend([2,4,6,[1,2,3]])
L1


# In[2]:


L1.append((8,9))
print(L1)


# In[3]:


L1.insert(0,1)
L1


# In[4]:


L1.remove(1)
L1


# In[5]:


#printing tuple
t=(1,2,3,4)
print(t)


# In[6]:


len(t)


# In[7]:


t.count(3)


# In[8]:


t.index(3)


# In[9]:


#creating set
s={1,2,3}
s


# In[10]:


s1={4,5,2}
s.union(s1)


# In[11]:


s.intersection(s1)


# In[12]:


s.difference(s1)


# In[14]:


s.add(4)
s


# In[17]:


s.clear()
s


# In[18]:


s1.pop()


# In[22]:


print(s1.discard(1))


# In[27]:


s2=s1.copy()
print(s2)


# In[34]:


s={0,1,2}
s1={2,3,4}
print(s.issubset(s1))


# In[35]:


#Creating dictionary
d={"name":"chinni","ID-No":"s181010"}
d


# In[36]:


d["name"]


# In[37]:


d.values()


# In[38]:


d.keys()


# In[39]:


d.popitem()


# In[40]:


d["class"]="2E"
d


# In[ ]:




