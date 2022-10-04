# Dicionários (dict)
# Estrutura que associa um chave a um determinado valor. É a representação do tão famoso objeto equivalente em outras linguagens

# Sintaxe:

people_by_id = {1: "maria", 2: "fernanda", 3: "felipe"} # elementos no formato "chave: valor"

people_by_name = {"maria": 1, "fernanda": 2, "felipe": 3} # outro exemplo, dessa vez usando string como chaves

# elementos são acessados por suas chaves
people_by_id[1] # saída: maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items() #dict_items([1, "maria"), (2, "fernanda"), (3, "felipe")])
# um conjunto de tuplas contendo chave e valor é retornado

# Bora fixar os aprendizados sobre dicts?

# Utilizando o código abaixo, faça os exercícios 8 e 9

info = {
    "personagem": "Margarida",
    "origem": "Pato Donald",
    "nota": "Namorada do personagem principal nos quadrinhos do Pato Donald",
}
# De olho na diga, em python precisamos colocar a chave do objeto entre aspas

# Insira no objeto uma nova propriedade com o nome de chave "recorrente" e o valor "sim". Em seguida imprima o objeto no console

# Remova a propriedade cuja chave é "origem" e imprima o objeto no console.

info.update({"recorrente": "sim"})
print(info)

# Usando o operador de descompactação

second = {"recorrente": "sim"}
dictionary = {**info, **second}
print(dictionary)

# Removendo a propriedade:

del dictionary["recorrente"]
print(dictionary)