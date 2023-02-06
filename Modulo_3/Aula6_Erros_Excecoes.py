#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Como tratar exceções?

# Try -> Operações que prevemos que por algum motivo pode dar errado.
# Except -> Código a ser executado caso a tentativa acima falhe.


# In[1]:


# ANTES
# No caso de o erro não estar tratado, nosso código, no momento em que encontra a exceção, ele quebra 

valor = 1000

parcelas = int(input("Número de parcelas: "))

valor_da_parcela = valor / parcelas

print("Ok! Nesse caso o valor de cada parcela é: ", round(valor_da_parcelas,2))


# In[2]:


# DEPOIS 
# Fazendo o tratamento de erro com try-except:

valor = 1000
parcelas = int(input("Número de parcelas: "))

try:
    valor_da_parcela = valor/parcelas
    print("Ok! Nesse caso o valor de cada parcela é: ", round(valor_da_parcela,2))
except:
    print("Algo está errado")
    
print("Será executado porque tratei o erro.")


# In[3]:


# Podemos mostrar qual foi o tipo do erro:

valor = 1000

try:
    parcelas = int(input("Número de parcelas: "))
    valor_da_parcela = valor/parcelas
    print("Ok! Nesse caso o valor de cada parcela é: ", round(valor_da_parcela,2))
except Exception as erro:
    print("Aconteceu um erro do tipo", erro.__class__, " e a mensagem de erro é: ",erro)
    
print("Será executado porque tratei o erro!")


# In[6]:


# Podemos ainda colocar uma exception para um tipo específico de erro:

valor = 1000

try:
    parcelas = int(input("Número de parcelas: "))
    valor_da_parcela = valor/parcelas
    print("Ok! Nesse caso o valor de cada parcela é: ", round(valor_da_parcela,2))
except ZeroDivisionError:
    print("Coloque um númmero diferente de 0")
except ValueError:
    print("Você só pode por números aqui.")


# In[ ]:




