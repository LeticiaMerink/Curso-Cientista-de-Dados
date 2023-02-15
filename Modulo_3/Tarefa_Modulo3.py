#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1- Construa uma função que recebe uma lista de tamanho 5 como parâmetro. Essa função deve percorrer cada elemento
# dessa lista e verificar se o elemento é par ou não. se ele for par, salvar ele em uma nova lista que deve ser retornada com 
# todos os valores pares encontrados.


# In[5]:


def identificaPares(lista): # construção da função sempre com def
    nova_lista = [x for x in lista if x%2==0]
    return nova_lista  # uma função SEMPRE tem do retorno

lista = [1,2,3,4,5]
nova_lista = identificaPares(lista) #nova_lista recebe o retorno da função identificaPares


print(nova_lista)


# In[5]:


# 2 - Escreva um código que chama o módulo random. Dentro deste módulo utilize a função que gera números aleatórios inteiros
# para criar uma função customizada que pede para o usuário digitar quantidade de sorteios que ele quer e roda
# sorteando essa quantidade de números. Alguns usuarios podem não entender que o input é um número e digitar por exemplo
# "três", o que geraria um erro no codig. Então escreva essa função de maneira a tratar esse erro, enviando uma mensagem
# que ajude o usuário a resolver o problema.


# In[10]:


import random

try:
    usuario = (int(input("Digite um número de 1 a 50: ")))
except ValueError:
    print("Você só pode por números.")

    
for i in range(usuario): # para cada i dentro de um range(usuario) 
    print("Número gerado: ", random.randint(1,51)) # vai gerar números aleatorios de 1 até 50


# In[7]:


# 3- Crie uma classe cliente. Esse cliente deve possuir 2 atributos: nome e saldo e 2 métodos: depositar e sacar. Usando
# a classe, crie um cliente, utilize os métodos criados para depositar 100 reais na conta do cliente, que deve começar
# com o saldo 0 e depois do depósito apresentar saldo 100. na sequência, faça um saque de 20 reais. Fique atento: o seu
# código deve impedir que o usuário saque mais do que ele tem em saldo.


# In[3]:


class Cliente:
    
    # Atributos
    def __init__(self, nome, saldo): # __init__ é o método construtor
        # o self é necessário porque quando você quiser construir de fato um veículo, vc passará os atributos dele e o
        # programa vai entender que eles serão atribuídos a esse objeto mesmo que tá sendo criado.
        self.nome = nome
        self.saldo = 0 
        
    # Métodos
    def imprimeSaldo(self):
        print("Saldo: R$ ", self.saldo)
        
    def depositar(self, valor):
        self.saldo += valor
        print("Seu novo saldo é: R$ ", self.saldo)
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= self.saldo - valor
            print("Valor sacado: R$ ", self.saldo)
            return True
        else:
            print("Saldo indisponível.")
            return False   


# In[4]:


cliente = Cliente("Leticia", 0)
print(cliente.nome)

cliente.imprimeSaldo()
cliente.depositar(100)
cliente.sacar(20)
cliente.imprimeSaldo()


# In[ ]:




