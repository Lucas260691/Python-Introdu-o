# Estruturas de repetição

# for exemplo:
# Imagine um sistema que faça a listagem de restaurantes.Estes restaurantes possuem um nota proveniente de avaliação dos seus clientes.

from math import factorial


restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

# Quando um cliente pede a listagem de restaurantes, ele pode escolher filtrar o resultado de acordo com a nota. Essa filtragem pode ocorrer percorrendo a lista de restaurantes ou criando uma nova lista com somente aqueles que atendem ao filtro, assim como mostra no exemplo abaixo:

filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants) # imprime a lista de restaurantes, sem o B e D

# Dado que a maior parte do tempo estamos percorrendo estruturas, os criadores do Python decidiram que o for each seria o laço de repetição principal da linguagem

# Para cada repetição do nosso laço, um novo elemento de estrutura iterável é atribuído a varíavel de iteração. No exemplo acima, vemos que a cada iteração um novo restaurante é colocado na varíavel restaurant.

# Em alguns casos, podemos ainda querer percorrer uma sequência numérica, e para isto iteramos sobre a estrutura de dados range.

for index in range(5):
    print(index)

# Compreensão de lista (list comprehension)

# A compreensão de listas em python possui uma sintaxe fácil e compacta para criação de listas, seja a partir de uma string ou de outra lista. É uma maneira concisa de criação que executa uma operação em cada item da lista já existente.

min_rating = 3.0
filtered_restaurants = [restaurant
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants) # imprime a lista de restaurantes, sem o B e D

# A compreensão de listas é declarada da mesma maneira que uma lista comum, porém no lugar dos elementos nós colocamos a iteração que vai gerar os elementos da nova lista.

team = ["Ana", "Rafa", "Duda", "André", "Jean"]
a_names = [name.upper() for name in team if name[0] == "A"]
# Saída: ["ANA", "ANDRÉ"]

# A compreensão de listas também funciona com listas de strings. A seguinte cria uma nova lista de strings com os nomes que contém a letra 'a'

name_list = ['Duda', 'Rafa', 'Cris', 'Yuri']
new_name_list = [name for name in name_list if 'a' in name]

# Aqui o for percorre cada nome em "names_list", verifica se existe a letra "a" nele,
# o adiciona á variável "name", e então gera nossa nova lista "new_names_list"
print(new_name_list)

#saída
['Duda', 'Rafa']

# O exemplo a seguir usa uma compreensão de listas para criar uma lista com o quadrado dos números entre 1 e 10
quadrados = [x*x for x in range(11)]
print(quadrados)

# Saída
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Isto é equivalente as operações map e filter em JS.

# While 
# A Sequência de Fibonacci, muito presente em diversas formas na natureza, é uma sequência numérica começando por 0 e 1 e cada termo subsequente correspondente á soma dos dois anteriores.
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next

# O laço de repetição while acontecerá enquanto a condição for satisfeita.
# No exemplo anterior, estamos imprimindo os elementos da sequência até que atinja o valor 10. Neste caso, foi utilizado um truque chamado atribuição múltipla. Isto é, atribuição de vários valores a múltiplas variáveis ao mesmo tempo.
# Este truque pode ser utilizado também para fazer a troca de valores entre variáveis: a, b = b, a.

# Enumarete

# Em Python, um loop for geralmente é escrito como um loop sobre um objeto iterável. Isso significa que você não precisa de uma variável de contagem para acessar itens no iterável.

# Porém as vezes, pode acontecer de você querer um variável que muda em cada iteração do loop. Em vez de criar e incrementar uma variável você mesmo, você pode usar enumerate() do Python para obter um contador e o valor do iterável ao mesmo tempo!

languages = ["python", "java", "js"]

enumerate_prime = enumerate(languages)

# converte um objeto enumerate em uma lista
print(list(enumerate_prime))
# saída: [(0, 'python'), (1, 'java'), (2, 'js')]

# você pode destruturar (unpack) os itens da lista ou tupla:

languages = ["python", "java", "js"]

for index, language in enumerate(['python', 'java']):
    print(f'{index} - {language}')
#saída:
# 0 - python
# 1 - java

# Calculando o fatorial de um número

numero = int(input("fatorial de:"))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1
print(resultado)