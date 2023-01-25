#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# LISTAS // Listas: [1, 2.5, "dados", [4,8]] --> são MUTÁVEIS, aceita dados de vários tipos


# In[26]:


# Para criar listas usamos [] e separamos os valores por ,

lista_nomes = ["Sergio", "Maria", "Pedro"]

type (lista_nomes)


# In[27]:


lista_varios_tipos = [1, 2, True, [4, 5, 6]]

type (lista_varios_tipos)


# In[28]:


lista_vazia = []


# In[29]:


type (lista_vazia)


# In[30]:


print (lista_vazia)


# In[31]:


lista_inteiros = list ([1,2,3])


# In[32]:


lista_inteiros


# In[33]:


type (lista_inteiros)


# In[34]:


# para ver quantos elementos temos na lista usamos a FUNÇÃO len()

len (lista_nomes) # len () calcula o comprimento de uma lista


# In[35]:


print (len(lista_vazia))


# In[ ]:





# In[36]:


# ACESSANDO ELEMENTOS NA LISTA


# In[37]:


# a indexação em python começa em 0 e não em 1


# In[38]:


lista_varios_tipos


# In[39]:


lista_varios_tipos [0]


# In[40]:


lista_varios_tipos [3]


# In[41]:


# e se quisessemos pegar o 2º elemento do 4º elemento da lista


# In[42]:


lista_varios_tipos [3][1]


# In[43]:


lista_varios_tipos [4] # não existe um 5º elemento na posição 4


# In[ ]:





# In[44]:


# SLICING EM LISTAS


# In[45]:


lista_nomes


# In[46]:


# É um intervalo aberto a direita, ou seja, quando escrevemos até 2, o elemento da posição 2 não entra!
lista_nomes[0:2]


# In[47]:


lista_nomes[:2]


# In[48]:


# É um intervalo fechado a direita, ou seja, quando escrevemos de 1 até 3, o elemento da posição 1 entra!
lista_nomes[1:3]


# In[49]:


lista_nomes[1:2]


# In[50]:


lista_nomes[-1]


# In[51]:


lista_nomes[-2]


# In[52]:


# escreve a lista de trás para frente
lista_nomes[::-1]


# In[ ]:





# In[53]:


# STRINGD VS LISTAS


# In[54]:


lista_nomes


# In[ ]:





# In[55]:


lista_nomes[1]


# In[56]:


type(lista_nomes[1])


# In[57]:


lista_nomes[1][0]


# In[58]:


lista_nomes[1][3]


# In[59]:


# Lista mutáveis


# In[60]:


lista_nomes[0] = "Mariana"


# In[61]:


lista_nomes # mudou a lista... no lugar de Sergio salvou Mariana


# In[62]:


# String imutáveis


# In[63]:


x = "Dados"


# In[64]:


x[0] = 'd'


# In[65]:


# CONCATENANDO LISTAS


# In[66]:


lista_nomes


# In[67]:


lista_nomes_1 = ["Fabio", "Sabrina"]

lista_nomes_1


# In[68]:


lista_todos_nomes = lista_nomes + lista_nomes_1

lista_todos_nomes


# In[ ]:





# In[69]:


# FUNÇÕES BÁSICAS PARA LISTAS


# In[70]:


lista_inteiros = [1,2,3]

lista_inteiros


# In[71]:


min(lista_inteiros) # min nos diz o menor elemento da lista


# In[72]:


max(lista_inteiros) # max nos diz o maior elemento da lista


# In[73]:


sum(lista_inteiros) # soma dos elementos da lista


# In[74]:


type(lista_inteiros)


# In[75]:


len(lista_inteiros) # quantidade de elementos que existe na lista


# In[76]:


lista_range = list(range(0,10,1)) # range cria uma lista de 0 até 10 com intervalo de 1 nº

lista_range


# In[77]:


list(range(0,10,2)) # range cria um alista de 0 até 10 com intervalo de 2 em 2


# In[ ]:





# In[78]:


# FUNÇÕES NATIVAS PARA LISTAS


# In[79]:


# Já vimos que podemos adicionar elementos na lista concatenando com outra

linguagens = ["Python", "SQL", "R"]

linguagens_1 = linguagens + ["Java", "C++"]

linguagens_1


# In[80]:


linguagens_1.clear() # limpar a lista

print(linguagens_1)


# In[81]:


# lista.+ tab mostra funções nativas para listas - aprenderemos mais sobre funções no final do módulo
# append adiciona elemento no final da lista

linguagens.append("Java")
linguagens.append("C++")

linguagens


# In[82]:


linguagens.append(["Java", "C++"])
linguagens


# In[83]:


# extend adiciona outra lista como elementos da lista original e não como uma lista

linguagens.extend(["Java", "C++"])
linguagens


# In[84]:


# insert adiciona elementos em posição específicas da lista

linguagens.insert(1, "Scala") # Scala é add na posição [1]

linguagens


# In[85]:


# remove deleta o priimeiro elemento encontrado na lista com esse nome
linguagens.remove("C++")


# In[86]:


linguagens


# In[87]:


# pop remove elemento da lista usando indice

linguagens.pop(len(linguagens)-1)

linguagens


# In[88]:


linguagens.pop(2)

print(linguagens)


# In[89]:


# count conta quantidade de elementos na lista

linguagens.count("Java")


# In[90]:


# sort ordena os elementis da lista (Se for stribg, por ordem alfabetica)

lista_nomes.sort()
lista_nomes


# In[91]:


lista_range.sort()
lista_range


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




