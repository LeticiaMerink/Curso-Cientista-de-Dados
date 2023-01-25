#!/usr/bin/env python
# coding: utf-8

# In[3]:


nome = "Leticia" #definição da variável sempre o nome = valor (o "=" é chamado de operador de atribuição)


# In[8]:


idade = 34


# In[9]:


altura = 1.72


# In[10]:


e_matematica = True


# In[5]:


nome


# In[11]:


idade


# In[12]:


altura


# In[13]:


e_matematica


# In[17]:


nome = "Leticia"
idade = 34
altura = 1.72
e_matematica = True


# In[18]:


nome


# In[19]:


nome #se colocarnos as duas variaveis em um bloco ele mostrará apenas o valor da ultima
altura


# In[ ]:


nome, altura #podemos colocar dessa forma


# In[20]:


print (nome)
print (altura)


# In[21]:


print ("O valor da variável nome é: ", nome)


# In[ ]:





# In[ ]:


# VERIFICANDO OS TIPOS DE VARIÁVEIS


# In[22]:


type (nome) #type é o comando para saber o tipo da variável


# In[23]:


type (idade)


# In[24]:


type(altura)


# In[25]:


type(e_matematica)


# In[ ]:





# In[ ]:


# CONVERSÃO DE TIPOS


# In[ ]:


#supondo que agora queremos não apenas dizer os anos, mas os anos e meses, 
# então poderiamos escrever por ex: 34.11, 34 anos e 11 meses


# In[26]:


type (idade) # queremos converter o valor int para float


# In[33]:


float (idade) #aqui aind anão convertemos'


# In[34]:


type (idade)


# In[35]:


idade = float (idade)


# In[36]:


type (idade)


# In[37]:


type (nome)


# In[38]:


float (nome) # não conseguimos converter por exemplo, uma string em um float


# In[39]:


float (e_matematica) #true = 1, false = 0


# In[ ]:





# In[ ]:


# SOBREESCREVENDO O VALOR DE UMA VARIÁVEL


# In[40]:


altura


# In[42]:


altura = "Olá"


# In[43]:


altura


# In[ ]:





# In[ ]:





# In[ ]:




