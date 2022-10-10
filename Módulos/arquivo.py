#Módulos

#Um módulo é um arquivo que contém definições e instruções em Python. O nome do arquivo é um nome acrescido de .py. Você pode importar um módulo dentro de um outro arquivo Python e ter acesso às suas funções, classes, etc.

#Em linhas gerais, todo arquivo que é escrito com a linguagem Python e com a extensão .py é considerado um módulo.

#Observe o arquivo my_math.py abaixo:


def sum(a, b):
  return a + b


def pot(a, b):
  return a ** b


print(sum(2, 2))
print(pot(2, 3))

#Este arquivo é um módulo Python, que pode ser executado como script com o comando python3 my_math.py. Se isso ocorrer, os retornos serão 4 e 8, respectivamente, devido às chamadas das funções dentro dos métodos print().

#Entretanto, as funções que criamos neste arquivo podem ser reaproveitadas por outros módulos através da declaração import.

#À medida que fomos avançando, esses conceitos ficarão cada vez mais nítidos.