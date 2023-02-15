#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# SQL

# Structured Query Language -> SQL é uma linguagem de consulta e persistência de dados (adicionar, alterar,
# excluir...)
# É uma linguagem usada para criar tabelas, manipular os dados das tabelas e principalmente, 
# consultar os dados.


# In[1]:


# SQLite

# SQLite é uma biblioteca que implementa um banco de dados SQL embutido

import sqlite3


# In[2]:


# Criando um banco de dados e estabelecando uma conezão com ele:

conn = sqlite3.connect("Primeiro_banco_dados.db") # precisa colocar a extenção .db pro python entender que estamos criando um banco de dadoss

print(conn)


# In[3]:


# Cursor e através dessa variável que criamos tabelas, inserimos registros e fazemos as queries de operações no banco
cursor = conn.cursor()


# In[ ]:


# IMPORTANTE: Nos bancos de dados relacionais salvamos os dados em tabelas. Essas tabelas possuem atributos(colunas) e
# os registros(linhas). No caso de DB's relacionais nós definimos as tabelas e os tipos de dados previamente. lembram
# que nos bancos não - relacionais é diferente? Nos não - relacionais não precisamos fazer isso!

#  * CREATE TABLE: Comando usado para criar tabelas

    # CREATE TABLE nome_tabela (coluna1 tipo, coluna2 tipo...);
# Geralmente usamos letras maiúsculas para escrever os cmandos em linguagem SQL;


# In[4]:


# Criando nossa primeira tabela. O método execute recebe um query SQL e a executa;

cursor.execute("CREATE TABLE cadastro_cliente (user_id integer, nome text, idade integer, cidade text, email text)")


# In[5]:


# Usamos essa query para ver quais as tabelas estão no banco.
cursor.execute('SELECT name from sqlite_master where type= "table"')

# O comando fetchall é responsável por apresentar o resultado da query
cursor.fetchall()


# In[6]:


# SELECT --> usamos esse comando para selecionar dados na tabela

# Vamos ver o que tem nessa nossa tabela?
# * == ALL: Seleciona todos os campos (atributos e colunas) da tabela

cursor.execute("SELECT * FROM cadastro_cliente")
cursor.fetchall()


# In[ ]:


# INSERT INTO --> Usado para inserir registros em uma tabela
# Os dados do tipo text precisam estar com as strings que aprendemos aqui em python e tem que ser aspas simples, porque
# estamos usando aspas dupllas para a query, se não o python faz confusão


# In[7]:


# Precisamos dizer em qual tabela e também escrever no formato de dados previsto quando criamos a tabela:

cursor.execute("INSERT INTO cadastro_cliente VALUES(123, 'maria', 40, 'São Paulo', 'maria@gmail.com')")
conn.commit()

# Commit é um comando como no git, você deu um comando pali em cima para alterar a tabela e o commit é pra de fato
# guardarmos a informação no banco.


# In[8]:


# Verificando se nossa tabela foi de fato alterada:
cursor.execute("SELECT * FROM cadastro_cliente")
cursor.fetchall()


# In[9]:


# Vamos inserir agora 2 registros

cursor.execute("INSERT INTO cadastro_cliente VALUES (456, 'pedro', 22, 'rio de Janeiro', 'pedrinho@gmail.com')")
cursor.execute("INSERT INTO cadastro_cliente VALUES (789, 'joão', 35, 'São Paulo', 'joaojoao@gmail.com')")
cursor.execute("INSERT INTO cadastro_cliente VALUES (901, 'Paulo', 56, 'São Paulo', 'paulo123@gmail.com')")
conn.commit()


# In[10]:


# Visualizando todos os nossos registros:

cursor.execute("SELECT * FROM cadastro_cliente")
cursor.fetchall()


# In[ ]:


# SELECT DISTINCT -> Esse comando é usado para retornar apenas valores distintos

# SELECT DISTINCT coluna1, coluna2, ... FROM nome_tabela


# In[11]:


cursor.execute("SELECT cidade FROM cadastro_cliente")
cursor.fetchall()


# In[12]:


cursor.execute("SELECT DISTINCT cidade FROM cadastro_cliente")
cursor.fetchall()


# In[ ]:


# SELECT WHERE -> Seleciona dados de acordo com alguma condição. Usada para filtrar registros

# SELECT coluna1, coluna2, ... FROM nome_tabela WHERE condicao_verdadeira


# In[13]:


cursor.execute("SELECT * FROM cadastro_cliente WHERE nome = 'maria'")
cursor.fetchall()


# In[ ]:


# SELECT ORER BY ->  Seleciona dados ordenando em ordem crescente ou decrescente os dados com os valores
# de uma coluna específica.

# SELECT coluna1, coluna2, ... FROM nome_tabela ORDER BY coluna1, coluna2 ... DESC/ASC


# In[14]:


# vamos pedir para trazer os dados da maior para a menor idade
cursor.execute("SELECT nome, idade FROM cadastro_cliente ORDER BY idade DESC")
cursor.fetchall()


# In[ ]:


# SELECT GROUP BY -> Seleciona dados agrupando os dados por uma (+ de uma) coluna(s) específica(s)
# Quando a gente usa o GROUP BY  a gente tem que fazer uma sumarização nos campos que a gente vai trazer,
# a gente tem que aplicar uma função nesse campo. Eu não posso dar SELECT nome_campo e lá no fim
# fazer GROUP BY

# SELECT coluna1, coluna2, ... FROM nome_tabela GROUP BY coluna1...


# In[15]:


cursor.execute("SELECT COUNT(user_id), cidade FROM cadastro_cliente GROUP BY cidade")
cursor.fetchall()
# primeiro o SQL agrupa por cidade e em cada uma delas ele traz as cidades mas a outra informação que é o 
# user_id ele vai contar essa informação.
# Então ele vai ver quantos user_id tem em cada uma das cidades


# In[16]:


# Podemos fazer consultas mais complexas, como por exemplo:

cursor.execute("SELECT COUNT(user_id), cidade FROM cadastro_cliente GROUP BY cidade                 ORDER BY COUNT(user_id) DESC")
cursor.fetchall()


# In[17]:


# Criando outra tabela:

cursor.execute("CREATE TABLE compras_cliente (user_id integer, qtd_produtos integer,                  valor_compra decimal, local_compra text)")


# In[18]:


cursor.execute("INSERT INTO compras_cliente VALUES( 123,3 , 150.70, 'loja01')")
cursor.execute("INSERT INTO compras_cliente VALUES( 456,1 , 20.35, 'loja02')")
cursor.execute("INSERT INTO compras_cliente VALUES( 789,6 , 437, 'loja02')")
conn.commit()


# In[19]:


cursor.execute("SELECT * FROM compras_cliente")
cursor.fetchall()


# In[ ]:


# SELECT COUNT/AVG/SUM
# Count: Retorna o número de valores de uma determinada coluna.
# Avg: Retorna a média dos valores de uma determinada coluna.
# Sum: Retorna a soma dos valores de uma determinada coluna.

# SELECT COUNT/AVG/SUM(nome_coluna) FROM nome_tabela


# In[20]:


# Quantos usuários fizeram compras?
cursor.execute("SELECT COUNT(user_id) FROM compras_cliente")
cursor.fetchall()


# In[ ]:


# Quantos usuários fizeram compras na loja 01?
cursor.execute("SELECT COUNT(user_id) FROM compras_cliente WHERE local_compra=='loja01'")
cursor.fetchall()


# In[21]:


# Qual foi o valor_medio de gasto de cada usuário?
cursor.execute("SELECT AVG(valor_compra) FROM compras_cliente")
cursor.fetchall()


# In[22]:


# Qual foi o total gasto pelos usuários?
cursor.execute("SELECT SUM(valor_compra) FROM compras_cliente")
cursor.fetchall()


# In[ ]:


# E se quisessemos saber qual cidade tem um gasto médio maior? São Paulo ou Rio?
# cada informação está em uma tabela diferente, e agora? Let's join!

# A cláusula "join" é usada para combinar/relacionar linhas de duas tabelas baseado em uma 
# coluna comum entre eles (chamamos de chave) -- Banco de dados relacional

# Inner join: Retorna os registros que estão em ambas as tabelas
# Left join: Retorna todaos os registros da tabela da esquerda e traz os campos dos registris 
# da tabela da direita que deram match com a tabela da esquerda.
# Right join: Retorna todos os registros da tabela da direita e traz os registros da esquerda 
# que deram match com a tabela da direita.
# Full join: Retorna todos os registros quando tem um match com a tabela da direita ou da esquerda.


# In[ ]:


# no SQL é de boa pratica a gente colocar um eilhas (cc. e ccli.)  
# cc. -> é o nome da minha tabela cadastro_cliente
# ccli. -> é o nome da minha tabela compras_cliente


# In[23]:


# podemos fazer apenas primeiro um lef join por exemplo, pra ficar mais claro o que ele faz:

cursor.execute("SELECT cc.user_id, cc.nome, cc.cidade, ccli.valor_compra FROM cadastro_cliente as cc                LEFT JOIN compras_cliente as ccli ON cc.user_id == ccli.user_id")
cursor.fetchall()


# In[24]:


# Respondendo nossa pergunta ali de cima: Precisamos primeiro pegar todas as cidades, então vamos usasr
# a tabela cadastro_cliente e cruzar ela com a tabela de compras para termos os gastos dos clientes tambem.

# A chave/coluna que relaciona essas tabelas é a coluna user_id

cursor.execute("SELECT AVG(valor_compra) as valor_medio, cidade FROM cadastro_cliente                LEFT JOIN compras_cliente                ON cadastro_cliente.user_id == compras_cliente.user_id                GROUP BY cidade                ORDER BY valor_medio DESC")
cursor.fetchall()


# In[25]:


# Vejam agora a diferença com o inner join:

cursor.execute("SELECT cc.user_id, cc.nome, cc.cidade, ccli.valor_compra FROM cadastro_cliente as cc                INNER JOIN compras_cliente as ccli ON cc.user_id == ccli.user_id")
cursor.fetchall()


# In[ ]:




