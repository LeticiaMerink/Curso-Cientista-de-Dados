#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Módulos são arquivos de códigos python que agrupam instruções e definições sobre um determinado assunto


# In[1]:


def cadastra_cliente (nome,email,cpf):
    cliente = {}
    cliente['nome'] = nome
    cliente['email'] = email
    cliente['cpf'] = cpf
    return cliente

nome = str(input("Digite seu nome: "))
email = str(input("Digite seu email: "))
cpf = int(input("Digite o número do seu cpf: "))

cliente = cadastra_cliente(nome,email,cpf)


# In[3]:


import funcoes_clientes as fc # importando e conectando os módulos criados em outro arquivo .py (funcoes_clientes)


# In[4]:


# Nosso novo código limpo

nome = str(input("Digite seu nome: "))
email = str(input("Digite seu email: "))
cpf = int(input("Digite o número do seu cpf: "))

cliente1 = fc.cadastra_cliente(nome, email, cpf)
fc.verifica_cadastro_ja_existente(cpf)
fc.verifica_email_valido(email)


# In[ ]:


# PACOTES


# In[ ]:


# pacotes são conjuntos de módulos. Pacotes é um grande conjunto e módulos são sub-conjuntos


# In[ ]:


# Módulos são arquivos .py. Dentro de cada módulo tem suas funções.
# Pacotes são como pastas que dentro tem os módulos.

# FUNÇÔES estão dentro de MÓDULOS que estão dentro de PACOTES.


# In[ ]:


# Importando um pacote

# import pacote -- importa o pacote com todos os módulos que ele possui
# from pacote import modulo_1 -- importa um modulo especifico daquele pacote


# In[ ]:


# Pacotes sempre fiam no início da célula ou do código. O ideal é colocar todas as importações na primeira célula do seu cód.


# In[ ]:


# Utilizando pacotes do python desenvolvidos pela comunidade:


# In[5]:


# import é a maneira como 'conectamos' o pacote com o nosso cód
import datetime

#datetime é uma  biblioteca (um pacote), date é o módulo e taday a função
datetime.date.today()


# In[6]:


datetime. # datetime. + tab mostra todas os módulos disponiveis no datetime


# In[ ]:


# veja que o comando acima importou todos os módulos do pacote datatime, provavelmente sem necessidade, pois vamos
# usar apenas o date.


# In[7]:


# Podemos importar um módulo específico de um pacote

from datetime import date
date.today()


# In[11]:


from math import ceil, sqrt

num = int(input("Digite um número: "))
print("A raiz é: ", sqrt(num))
print("Arredondando para cima fica: ", ceil(sqrt(num)))


# In[12]:


# mais um exemplo, que usaremos muito ao longo do curso:

from matplotlib import pyplot

# Geralmente importado da seguinte maneira: import matpltlib.pyplot as plt


# In[13]:


pyplot.scatter([1,2,3],[4,5,6]) # [1,2,3] eixo x e [4,5,6] eixo y
pyplot.show()


# In[ ]:


# Criando nosso módulo retângulo


# In[14]:


import math

def area_ret(b,h):
    return b*h

def perimetro(b,h):
    p = 2*b + 2*h
    return p
    
def diagonal_ret(b,h):
    # a**2 = b**2 + c**2 nós queremos encontrar a
    a = b**2 + h**2
    a = math.sqrt(a)
    return a

b = 4
h = 6

print("Área: ", area_ret(b,h))
print("Perímetro: ", perimetro(b,h))
print("Diagonal: ", diagonal_ret(b,h))


# In[ ]:


# vamos agora criar um arquivo retangulo.py com as nossas funções


# In[25]:


# importando nosso módulo

import retangulo as r

b = 4
h = 6

print("Área: ", area_ret(b,h))
print("Perímetro: ", perimetro(b,h))
print("Diagonal: ", diagonal_ret(b,h))


# In[ ]:


# Para criar um pacote basta criar uma pasta e adicionar os módulos dentro dessa pasta


# In[26]:


# Criando um módulo círculo

import circulo as c

r = 3

print("Área: ", c.area(r))
print("Comprimento: ", c.comprimento(r))


# In[27]:


# Agora, vamos importar do nosso pacote nossos dois módulos, retangulo e circulo:

from meus_pacotes import circulo, retangulo


# In[47]:


print(circulo.area(2))
print(retangulo.area_ret(2,3))


# In[48]:


# Instalando pacotes

# !pip install nomedopacote


# In[4]:


get_ipython().system('pip install pandas-profiling')


# In[5]:


import pandas-profiling as pp


# In[6]:


pp.


# In[ ]:





# In[ ]:




