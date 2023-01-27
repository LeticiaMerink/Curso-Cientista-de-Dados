#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Estrutura de decisão são utilizadas quando queremos que o algoritmo tome caminhos diferentes de acordo com o valor de 
# alguma variável de innteresse.


# In[3]:


nota = 5

if nota >=7:
    print("Parabéns! Você está aprovado.")
else:
    print("Você foi reprovado. :/")


# In[4]:


# Criamos um programa onde perguntamos a idade par o usuário e verificamos se ele já está apto a tirar a carteira de motorista.
# Podemos escrever apenas o if, sem o else.

idade = int(input("Qual sua idade? "))

if (idade >= 18) :
        print("Idade digitada: ", idade)
        print("Você já pode tirar a carteira de motorista!")
        print("Parabéns!")


# In[6]:


idade = int(input("Qual sua idade? "))
visao = str(input("Você enxerga bem?"))

if (idade >= 18 and visao == "sim") :
    print("Você já pode tirar a carteira de motorista!")
    print("Parabéns!")


# In[10]:


# Ex: Suponha que criamos um programa para um supermercado. O usuário tem que ser capaz de conseguir pesquisar se um
# produto está disponível em estoque.

produtos_disponiveis = ["arroz", "feijão", "farinha", "banana", "leite"]
produto = input("Qual produto você procura? ")

if produto in produtos_disponiveis:
        print("Oba! Temos esse produto no estoque.")
        print("Corre enquanto da tempo.")
        print("Agradecemos a preferência!")


# In[11]:


# Suponha que no app do banco o usuário quer fazer um saque. Para isso, precisamos ver se ele tem o dinheiro, e se tiver,
# vamos liberar o saque e atualizar o saldo dele.

saldo = 1000
valor_saque = 75

if saldo >= valor_saque:
    print("O valor de ", valor_saque, "foi sacado com sucesso.")
    saldo = saldo - valor_saque # consegue colocar oparação dentro do if
    print("Seu novo saldo é: ", saldo)


# In[14]:


nota = 5

if nota >= 7:
    print("Aprovado!")
else:
    print("Reprovado.")


# In[15]:


# Suponha agora que para ser aprovado precisamos ter frequência >= 80% E nota >=7

nota = 9
frequencia = 77

if (nota >= 7 and frequencia >= 80):
    print("Aprovado!")
else:
    print("Reprovado.")


# In[16]:


# Suponha agora que para ser aprovado precisamos ter frequência >= 80% OU nota >=7

nota = 9
frequencia = 77

if (nota >= 7 or frequencia >= 80):
    print("Aprovado!")
else:
    print("Reprovado.")


# In[ ]:


# Estrutura if - elif - else
# elife = else + if
# Com sua estutura podemos fazer if's aninhados, colocando várias condições


# In[17]:


# Considere o seguinte: Se o aluno tiver nota >= 7 já está aprovado. Se não, se ele tiver frequencia >= 80
# ele fica de exame. Se ele não tiver nenhum dos dois, ele está reprovado.

nota = 5
frequencia = 77

if (nota >= 7):
    print("Aprovado")
else:
    if frequencia >= 80:
        print("Em exame.")
    else:
        print("Você não veio as aulas e tem nota baixa, está reprovado.")


# In[21]:


# Cód usando elif
nota = 6
frequencia = 85

if ( nota >= 7):
    print("Aprovado!")
elif nota >= 6 and frequencia >= 80:
    print("Em exame")
else:
    print("Você não veio as aulas e tem nota baixa, está reprovado.")


# In[ ]:





# In[ ]:




