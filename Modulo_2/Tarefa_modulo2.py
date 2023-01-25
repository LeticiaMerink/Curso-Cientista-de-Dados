#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ex1_a


# In[8]:


# criando 2 variáveis e fazendo a verificação se são iguais
nome = "Leticia"
sobrenome = "Merink"

print(nome)
print(sobrenome)
print(nome is sobrenome) # verificação


# In[ ]:


# Ex1_b


# In[17]:


var1 = 7
var2 = 3

print(var1)
print(var2)
print(var1%var2)


# In[ ]:





# In[24]:


# Ex2:

lista_strings = ["café", "arroz","feijão","arroz","açucar","sal","café"] # criando a lista
print(lista_strings)
print(len(lista_strings)) # tamanho da lista

print()

print(set(lista_strings)) # convertendo a lista em conjunto
print(len(set(lista_strings))) # tamanho do conjunto criado a partir da lista


# In[ ]:





# In[29]:


# Ex3
# Criando listas
lista_cliente = ["Maria" , "Joao", "Pedro"]
lista_produtos = [["caneta","lapis"], ["borracha", "apontador", "regua"], ["corretivo","tinta"]]
print(lista_cliente)
print(lista_produtos)

# unificando as listas
lista_cliente_prod = list(zip(lista_cliente,lista_produtos))
lista_cliente_prod

# transformando lista em dicionário
dic_cliente_prod = dict(lista_cliente_prod)
print(dic_cliente_prod)


# In[ ]:





# In[ ]:




