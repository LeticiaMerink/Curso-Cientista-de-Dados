#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ESTRUTURAS DE REPETIÇÃO
# são utilizadas quando queremos que um bloco de código seja executado mais de uma vez.
# FOR ; para
# WHILE ; enquanto


# In[ ]:


# Loop FOR é usado quando queremos executar um bloco de código um número fixo de vezes.
# loop WHILE é usado quando queremos repetir um bloco de código enquanto uma condição é verdadeira.


# In[ ]:


# LOOP FOR


# In[2]:


# podemos iterar em listas (precisa ser um objeto iterável):

# roda um número fixo de vezes, nesse caso 5.
for num in range(1,10,2): # vamos de 1 até 10 pulando de 2 em 2
    print(num)


# In[3]:


# podemoss iterar em strings:

for letra in "PYTHON":
    print(letra)


# In[9]:


# podemos iterar em dicionários:

dic_aluno_nota = {"Maria" : 7.5, "João" : 9, "Pedro" : 6, "Mariana" : 10, "Paulo" : 6.5}
# Podemos ver a nota de um único aluno fazendo:
print(dic_aluno_nota["Maria"])


# In[10]:


# Para analisarmos a nota de todos os alunos não faz zentido escrevermos esse código acima varias vezes.
# Usmos um loop for para isso.

# duas variáveis iteradoras, a chave e o valor

for aluno, nota in dic_aluno_nota.items():
    print(aluno, ":", nota)


# In[11]:


# Podmeos combinar o loop for com a estrutura if-else para termos códigos ainda mais poderosos.

alunos_reprovados = {}
alunos_aprovados = {}

for aluno, nota in dic_aluno_nota.items():
    if nota < 7:
        alunos_reprovados.update({aluno:nota})
    else:
        alunos_aprovados.update({aluno:nota})


# In[12]:


alunos_reprovados


# In[13]:


alunos_aprovados


# In[ ]:


# Alterar a execução do loop

# Podemos alterar a execução de um loop usando break ou continue


# In[16]:


# break: usado para sair de um loop (para o loop), não importando o estado em que se encontra

lista_1 = range(1,50,2) # i
lista_2 = range(1,50,1) # j

for i,j in zip(lista_1,lista_2):
    if i*j >100:
        break
    else:
        print(" i x j é: ",i*j)
        
print("Aqui o loop já parou!")
print("Os próximos i e j seriam: ", (i,j))


# In[17]:


# continue: Ao inves de parar o loop, ele faz com que todo o código que esteja abaixo seja ignorado e 
# avança para a próxima iteração.

lista_1 = range(1,50,1)

for i in lista_1:
    if(i % 2 == 0):
        print("Esse número é par: ",i)
    else:
        continue


# In[ ]:





# In[ ]:


# LOOP WHILE


# In[18]:


#Ex: suponha que estamos construindo um modelo de ML(machine larning). Queremos rodar esse código até que nosso modelo 
# tenha um erro menor que um determinado valor, digamos 11.

erro = 30

while erro > 11:
    print("O erro ainda é maior que 11, é: ", erro)
    erro = erro - 2 # sem essa linha o while nunca pararia
    
print("\n fim do while com erro igual a ", erro)


# In[ ]:





# In[ ]:





# In[ ]:




