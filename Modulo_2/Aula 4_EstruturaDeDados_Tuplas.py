#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TUPLAS // Tuplas: (1,2,3,2) --> são IMUTÁVEIS (altera a tupla toda apenas), aceita dados de vários tipos


# In[1]:


## para criar tuplas usamos () e separamos os valores por ,

tupla_inteiros = (1,2,3)


# In[2]:


print(tupla_inteiros)


# In[3]:


type(tupla_inteiros)


# In[4]:


# Podemos criar usando o metodo tuple

tupla1 = tuple((1,2,"a", True, "a"))


# In[5]:


tupla1


# In[6]:


type(tupla1)


# In[7]:


print(len(tupla_inteiros))
print(len(tupla1))


# In[8]:


# Acessando elementos da tupla

tupla1


# In[9]:


tupla1[2]


# In[10]:


tupla1[-1]


# In[11]:


# Concatenando tuplas

tupla1 + tupla_inteiros


# In[12]:


# Funções básicas para

print(max(tupla_inteiros))
print(min(tupla_inteiros))


# In[13]:


# imutável!

tupla_inteiros[0] = 2


# In[ ]:


# tuplas não tem muitos métodos


# In[16]:


tupla1.count('a')


# In[17]:


tupla1.index('a')


# In[ ]:





# In[ ]:




