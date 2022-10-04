# Um conjunto é uma coleção de elementos únicos e não ordenados. Conjuntos implementam operações de união, intersecção e outras.

# Sintaxe:

permissions = {"member", "group"} # elementos separados por vírgula, envolvidos por chaves

permissions.add("root") # adiciona um novo elemento ao conjunto

permissions.add("member") # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"}) # retorna um conjunto resultado da união

permissions.intersection({"user", "member"}) # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"}) # retorna a diferença entre os dois conjuntos

name = set()
name.add("Lucas Sodré")
print(name)

# Um conjunto ou set pode ser inicializado utilizando-se também o método set(). Inicialize uma variável com essa função var = set() e adicione seu nome ao conjunto utilizando um dos métodos acima.Depois, imprima a variável e confira se o retorno é: {"seu nome"}


# Conjuntos Imutáveis (fronzenset)

# É uma variação do set, porém imutável, ou seja, seus elementos não podem ser modificados durante a execução do programa

permissions = frozenset(["member", "group"]) # assim como o set, qualquer estrutura iterável pode ser utilizada para criar um frozenset

permissions.union({"user"}) # novos conjuntos imutáveis podem ser criados á partir do original, mas o mesmo não pode ser modificado

permissions.intersection({"user", "member"}) # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"}) # retorna a diferença entre os dois conjuntos

