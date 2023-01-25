#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# DICIONÁRIOS // DICIONÁRIOS: {"AI":1, "ML":2, "DL":[3,4]} --> são MUTÁVEIS, conceito de chave-valor


# In[ ]:


# Dicionário diferentemente da tupla e lista, ele não é uma coleção de elementos, ele é uma coleção de pares de elementos.


# In[ ]:


##  - KEYS - 'a' 'o' 'g'  - VALUES - 'alpha' 'omega' 'gamma'


# In[1]:


dicionario = {}


# In[2]:


dicionario


# In[4]:


type(dicionario)


# In[ ]:


len(dicionario)


# In[5]:


# podemos usar também a função dict()

dicionario = dict()


# In[6]:


dicionario


# In[ ]:


# dicionario = {chave: valor} -- chave pode ser string, int...
# Ex: Suponha que eu como professora queria guardar as notas de vocês auqi no curso.


# In[ ]:


notas = {10,9.5,8,7,7.5} # de quem é cada nota? como vou saber se a nota 10 é do João ou da Maria?


# In[4]:


# Uma melhor opção seria o dicionário.

primeiro_dict = {"Joao":10, "Maria":7.5, "Pedro":6}


# In[5]:


# As chaves devem ser únicas!


# In[6]:


primeiro_dict


# In[7]:


# Adicionando o par (João, 9) no primeiro_dict

primeiro_dict["Joao"] = 9


# In[8]:


primeiro_dict


# In[9]:


primeiro_dict["mariana"] = 8.7


# In[10]:


primeiro_dict


# In[11]:


primeiro_dict.update({"Joaquim": 7.7})


# In[12]:


primeiro_dict


# In[13]:


len(primeiro_dict)


# In[14]:


# A inspiração é um dicionario mesmo, que a gente conhece, por exemplo, um dicionario ingles/portugues:

dic_en_pt = {"data science": "ciencia de dados",
            "Machine Learning": "Aprendizado de Máquina",
            "Deep Learning": "Aprendizado Profundo"}


# In[15]:


dic_en_pt


# In[ ]:





# In[16]:


# ACESSANDO OS VALORES


# In[17]:


primeiro_dict


# In[18]:


# Acessando valores via chave

primeiro_dict["Joao"]


# In[19]:


primeiro_dict.get("Joao")


# In[20]:


# Lembrando que o Python é case sensitive? Não tem João com j minusculo como chave.

primeiro_dict.get("joao")


# In[21]:


# Indexação é pela chave não pela posição como nas listas

primeiro_dict[0]


# In[22]:


# ALTERANDO VALORES


# In[23]:


primeiro_dict


# In[24]:


# Dicionário é mutável
primeiro_dict["Pedro"] = 6.5


# In[25]:


primeiro_dict


# In[26]:


# valores podem ser: int, str, boo, listas, tuplas... FALAR: supor que voce faz 2 cursos aqui, DS beginer
# e o pro, então eu quero gravar para cada aluno a nota final nos dois cursos, eu posso?

dic_duas_notas = {"Joao": [9,9.5], "Maria": [7.5,8], "Pedro": [6.5,6], "Mariana": [8.7,9]}


# In[27]:


dic_duas_notas


# In[28]:


# podemos ter dicionários com valores de varios tipos por exemplo
# um dicionario que guarda imformações de um formulário

dic_form = {"nome": "Joao", "idade": 18, "nota1": 9, "nota2": 9.5, "aprovado": True}


# In[29]:


dic_form


# In[30]:


# podemos ter ainda dicionarios com chaves de varios tipos por exemplo

d = {"nome": "Joao", 1:9, 2:9.5}
print (d)


# In[31]:


type(d)


# In[32]:


print(d["nome"], d[1])


# In[ ]:





# In[33]:


# FUNÇÕES PARA DICIONARIOS


# In[ ]:


primeiro_dict.


# In[36]:


# já vimos a função get, usada para acessar elementos:

primeiro_dict.get("Pedro")


# In[37]:


# keys(): mostra todas as chaves do dicionário

primeiro_dict.keys()


# In[38]:


# values: mostra todos os valores do dicionário

primeiro_dict.values()


# In[39]:


# items(): mostra todos os itens (pares chave:valor) do dicionário - é o mesmo que dar print no dicionário

primeiro_dict.items()


# In[41]:


# pop(): remove a o par chave valor, com chave maria

primeiro_dict.pop("Maria")


# In[42]:


# update: Podemos usar para concatenar dois dicionários, alternando/mantendo valores caso a chave já exista.
# Se não existir ele cria.

print("Como era o primeiro dict",primeiro_dict)

segundo_dict = {"Maria": 7, "Sabrina": 5, "Joao": 9.2}

# altera a estrutura do primeiro_dict
primeiro_dict.update(segundo_dict)

print("Como ficou o primeiro dict", primeiro_dict)


# In[44]:


# clear: apaga os itens do dicionário

primeiro_dict.clear()
print(primeiro_dict)


# In[ ]:


# E como poderíamos pegar duas listas separadas e converter em um dicionário, sem ter que fazer de forma manual?


# In[ ]:


# Ex: Suponha que tivéssemos inicialmente uma lista de notas.
# Esses dados estão ordenados, isto é, o primeiro nome na lista 1 correspone a primeira nota na lisra 2 e assim 
# por diante. Como fariamos pra criar esse dicionário?

# utiliza-se a FUNÇÃO ZIP


# In[46]:


lista_nomes = ["Maria", "Joao", "Pedro", "Mariana"]
lista_notas = [7.5, 9, 6.5, 8.7]

print(lista_nomes)
print(lista_notas)


# In[47]:


# criamos uma lista com tuplas, que serão nossos pares chave; valor no dicionário
lista_pares = list(zip(lista_nomes, lista_notas)) ; lista_pares


# In[48]:


dicionario_nome_nota = dict(lista_pares)
print(dicionario_nome_nota)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




