#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# CONJUNTOS// Conjuntos: {1,2,3} --> são MUTÁVEIS, não ordenado, elementos únicos


# In[ ]:


# Conjuntos não possuem uma noção de ordem nem dados repetidos, 
# então seus elementos não podem ser acessados com colchetes [] nem podem ser fatiados.
# Conjuntos só aceitam tipos de dados imutáveis como inteiros, floats, tuplas e strings, 
# não aceitando listas, dicionários e outros conjuntos(set.)


# In[ ]:


# Criando Conjuntos


# In[19]:


# Usa chaves também, porém não temos pares e sim elementos
primeiro_conjunto = {2,4,6,8}


# In[20]:


# Não mantém a ordem - conjunto não é um objeto ordenado
print(primeiro_conjunto)


# In[21]:


type(primeiro_conjunto)


# In[22]:


len(primeiro_conjunto)


# In[23]:


# função SET()
# conjuntos não permitem elementos repetidos

lista_ = [1,2,5,6,6,7,8,8]

print(len(lista_)) # comprimento da lista
print(set(lista_)) # convertendo uma lista -> lista_ em um conjunto -> set
print(len(set(lista_))) # comprimento do conjunto criado a partir da lista 


# In[24]:


# podemos criar conjuntos vazios
conj_vazio = set()
dic_vazio = {}


# In[25]:


type(conj_vazio)


# In[26]:


type(dic_vazio)


# In[27]:


# Funções nativas para conjuntos


# In[28]:


# add(): Adiciona elementos

primeiro_conjunto.add(10)
primeiro_conjunto


# In[29]:


# remove um elemento do conjunto
primeiro_conjunto.pop()


# In[30]:


# remove o elemento que você nomear
primeiro_conjunto.remove(4)


# In[31]:


primeiro_conjunto


# In[ ]:





# In[ ]:


# OPERAÇÕES ENTRE CONJUNTOS


# In[ ]:


# Ex: Suponha que você tem duas listas e quer saber que elementos estão nas duas, isto é, estão na primeira lista
# e na segunda lista?


# In[32]:


pares = [2,4,6,8,10] # elementos pares
multiplos_4 = [4,8,12,16] # elementos multiplos de 4

pares = set(pares)
multiplos_4 = set(multiplos_4)


# In[33]:


print(type(pares))
print(type(multiplos_4))


# In[34]:


# Intersecção: Elementos que estão em pares E em multiplos de 4

pares.intersection(multiplos_4)


# In[35]:


# União: elementos que estão em pares OU em múltiplos de 4

pares.union(multiplos_4)


# In[37]:


# Diferença (pares - multiplos de 4): Elementos que estão em pares E NÂO estão em múltiplos de 4

pares.difference(multiplos_4)


# In[ ]:





# In[ ]:





# In[ ]:




