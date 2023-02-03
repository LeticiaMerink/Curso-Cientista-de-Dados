#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# POO é composto por objetos.

# OBJETOS: é algo MATERIAL ou ABSTRATO, que pode ser descrito por suas CARACTERÍSTICAS e COMPORTAMENTOS.
# esses objetos possuem propriedades e operações.
# Propriedades: são os atributos (características)
# Operações: são os métodos(comportamento) e as funções

# CLASSES: MOLDE que descreve os atributos e métodos de um determinado tipo de objeto (ideia abstrata de um tipo de objeto)
# essas classe possuem características(atributos) e comportamentos(métodos)


# In[ ]:


# Quando estruturamos algo orientado a objeto TUDO É OBJETO e como já vimos, os objetos tem duas principais coisas
# associadas a ele -métodos e atributos.
# Então a primeira coisa seria pensar no nosso programa para definir quais são os objetos, o que queremos representar? E 
# depois definir os atributos e métodos.

# MOTIVAÇÂO: Supondo que eu quisesse construir um jogo. Nesse jogo tem vários elementos: pessoas, animais, veículos
# casas... enfim, vários elementos que podem ser modelados como objetos. Vamos representar aqui veículos, para isso vamos fazer
# uma classe veiculos para que consigamos representar todos os meios de transporte do jogo.

# 1 - Planejar atributos / caracteristicas de um veículo como por ex(rodas, cor, marca, o ano)
# 2 - Métodos, ou seja, ligar, desligar, acelerar, abastecer...

# listaremos as características (atributos dos veículos) aqui:
# n_rodas
# cor
# marca

# listaremos agora os metodos:
# ligar()
# desligar()
# acelerar()


# In[5]:


# Criando classes e atributos
# CLASSE por convenção começa com letra MAiÚSCULA

class Veiculo:
    
    def __init__(self, n_rodas, cor, marca): # __init__ chama-se construtor
        # o self é necessário porque quando você quiser construir de fato um veículo, vc passará os atributos dele e o
        # programa vai entender que eles serão atribuídos a esse objeto mesmo que tá sendo criado.
        self.n_rodas = n_rodas
        self.cor = cor
        self.marca = marca
        self.velocidade = 0


# In[6]:


# Criando nosso primeiro veículo

veiculo1 = Veiculo(4, "branco", "ford")

print(veiculo1.cor)
print(veiculo1.marca)


# In[8]:


# Usando "objeto." podemos ver todos os atributos e métodos desse objeto:
veiculo1.velocidade  # veiculo1. + tab aparece todos os atributos


# In[9]:


# Podemos ver o tipo desse objeto, assim como tinhamos objetos listas, dicionários...

type(veiculo1)


# In[14]:


# Criando métodos para nossos veículos

class Veiculo:
    
    def __init__(self, n_rodas, cor, marca): # __init__ chama-se construtor
        # o self é necessário porque quando você quiser construir de fato um veículo, vc passará os atributos dele e o
        # programa vai entender que eles serão atribuídos a esse objeto mesmo que tá sendo criado.
        
        # Atributos
        self.n_rodas = n_rodas
        self.cor = cor
        self.marca = marca
        self.velocidade = 0
        
        # Métodos
    def ligar(self):
        print("O veículo ligou! vrummm")
            
    def desligar(self):
        print("O veículo desligou!")
            
    def acelerar(self):
        self.velocidade += 10
        print("Você acelerou! Sua velocidade atual é: ", self.velocidade)


# In[15]:


veiculo1 = Veiculo(4, "branco", "ford")

veiculo1.ligar()
veiculo1.acelerar()
veiculo1.acelerar()
veiculo1.acelerar()
veiculo1.desligar()


# In[16]:


veiculo1.velocidade


# In[ ]:


# HERANÇA

# E se quiséssemos agora criar uma moto, eu teria que criar uma classe moto? Moto é um tipo de veículo né?!
# Moto é um subconjunto de veículo certo? Veículo é um termo bem abrangente - que é justamente a ideia de classe.
# Se quisermos criar um tipo de veículo com caracteristicas específicas, com alguns metodos específicos, em python,
# podemos criar uma subclasse de veículos. Então moto seria uma subclasse de veículos.


# In[ ]:


# Na POO a gente o conceito de HERANÇA --> que significa subclasses das Classes
# Conseguimos herdar métodos e atributos da Classe Principal


# In[23]:


class Moto():
    def __init__(self, n_rodas, cor, marca):
        Veiculo.__init__(self, n_rodas, cor, marca)


# In[24]:


# Precisamos passar como parâmetro da classe Moto a classe veículo para definir a herança:

# quando cria a classe moto passa como parâmetro a classe principal Veiculo para o python entender que a classe Moto herda da classe Veiculo
class Moto(Veiculo): 
    def __init__(self, n_rodas, cor, marca):
        Veiculo.__init__(self, n_rodas, cor, marca)


# In[25]:


moto1 = Moto(2,"preta", "honda")

moto1.cor, moto1.marca, moto1.n_rodas


# In[26]:


type(moto1)


# In[27]:


# também herdamos os métodos:

moto1.ligar()


# In[28]:


moto1.acelerar()
moto1.acelerar()


# In[ ]:


# Podemos adicionar alguns métodos que so fazem sentido pra moto? Podemos mudar métodos herdados?


# In[31]:


class Moto(Veiculo):
    def __init__(self, n_rodas, cor, marca):
        Veiculo.__init__(self, n_rodas, cor, marca)    
    
    # Alterandoum método herdado:
    def acelerar(self):
        self.velocidade+=5 # em Veiculos o valor era 10, consigo alterar para 5
        print("Você acelerou! Sua velocidade atual é: ", self.velocidade)
        
    # Adicionando um metodo apenas em moto
    def empinar(self):
        print("A moto está andando sobre uma roda só! Cuidado.")


# In[32]:


moto2 = Moto(2, "azul", "BMW")

moto2.cor, moto2.marca, moto2.n_rodas, moto2.velocidade


# In[33]:


moto2.ligar()
moto2.acelerar()
moto2.acelerar()
moto2.acelerar()
print(moto2.velocidade)


# In[34]:


moto2.empinar()


# In[ ]:


# vVeiculo não tem o método empinar
veiculo1.


# In[ ]:





# In[ ]:




