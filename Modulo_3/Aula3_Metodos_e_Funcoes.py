#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# METODOS: São blocos de instruções, com nome único e que NUNCA retorna valores.
# FUNÇÕES: É um bloco de instrução, com nome único e que SEMPRE retorna valores.


# In[9]:


# Usando funções built-in

lista = [1,2,3,4,5]
print(min(lista))
print(max(lista))


# In[10]:


# função round

x = 3.5
round(x) # arredondando o valor de 3.5 para 4


# In[11]:


# Relembrando algumas funções de listas e dicionários

l = ["a", "b", "c"]

l.append("d")
l.remove("c")

print(l)


# In[12]:


dic = {"ola":"hello", "oi":"hi", "ei":"hey"}
dic.update({"tchau":"bye"})
print(dic)


# In[13]:


# help é uma função muito importante. Ela nos dá a descrição do uso das funções:
help(min)

# também podemos usar: funcao(clicar shift + tab com o cursor aqui dentro)
#min(shift+tab)


# In[14]:


# CRIANDO MÉTODOS

# para criar métodos fazemos da seguibte maneira:


# In[15]:


# def bome_da_funcao():
#      bloco de código


# In[16]:


# definindo o método:

def diz_oi():
    print("Faaaala galera")


# In[17]:


# executando a função:
diz_oi()


# In[18]:


oi = diz_oi()


# In[19]:


oi


# In[20]:


# Métodos com parâmetros

def ao_quadrado(x):
    print("O valor ao quadrado é: ", x**2)


# In[21]:


# Atenção: Agora precisamos passar o parâmetro na chamada da função

valor_ao_quadrado = ao_quadrado(10)


# In[22]:


valor_ao_quadrado


# In[ ]:





# In[23]:


# CRIANDO FUNÇÕES


# In[24]:


# def nome_da_funcao():
#    bloco de código
#    return()


# In[25]:


def func_ao_quadrado(x):
    return (x**2)


# In[26]:


valor_ao_quadrado = func_ao_quadrado(10)
valor_ao_quadrado


# In[27]:


# podemos ter mais de um parâmetro:

def soma(x,y):
    return x + y


# In[28]:


retorno_soma = soma(100,75); retorno_soma


# In[29]:


# utilizando estrutura if-else

def identifica_pares(x):
    if x % 2 == 0:
        print(x, "é par")


# In[30]:


identifica_pares(10)


# In[40]:


# utiliza a estrutura for:

def identifica_pares_na_lista(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            continue
    return pares


# In[41]:


pares_lista = identifica_pares_na_lista([1,2,3,4,5,6,7,8,9,10])
pares_lista


# In[42]:


type(identifica_pares_na_lista)


# In[43]:


help(identifica_pares_na_lista)


# In[44]:


def identifica_pares_na_lista(lista):
    """\n
    Retorna lista de números pares na lista de input.
    """
    
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            continue
    return pares


# In[45]:


help(identifica_pares_na_lista)


# In[ ]:


# Para determinados programas, códigos que queremos fazer, podemos construir um arquivo com as nossas próprias funções
# e depois podemos rodar aqui no notebook. --> funcs.py


# In[46]:


# são esses dois comandos que utiizamos para conectar os 2 arquivos ( minhas_funcs.py e esse Aula3_Met...)
# usa-se qualquer um dos dois

# %load minhas_funcs.py
# import minhas_funcs as f.


# In[ ]:


# %load minhas_funcs.py
def soma(x,y):
    return x+y

def multiplica(x,y):
    return x*y

def encontra_max_lista(lista):
    return max(lista)

def verifica_se_e_par(x):
    if x % 2 == 0:
        print(x, "é par")


# In[55]:


encontra_max_lista([1,3,5])


# In[56]:


verifica_se_e_par(5)


# In[58]:


verifica_se_e_par(2)


# In[59]:


import minhas_funcs as f


# In[60]:


f.encontra_max_lista([1,3,5])


# In[61]:


f.verifica_se_e_par(2)


# In[ ]:





# In[ ]:





# In[ ]:




