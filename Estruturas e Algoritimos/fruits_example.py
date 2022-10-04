fruits = ["laranja", "maca", "uva", "abacaxi"] # elementos são definidos  separados por virgula;

print(fruits[0]) # acesso é feito por índices iniciados em 0

print(fruits[-1]) # o acesso também pode ser negativo

fruits.append("banana") # adicionando um nova fruta
print(fruits)

fruits.remove("abacaxi") # remove uma fruta
print(fruits)

fruits.extend(["pera", "melão", "kiwi"]) # acrescenta uma lista de frutas a lista original
print(fruits)

fruits.index("maca") # retorna o índice onde a fruta está localizada, nesta caso 1
print(fruits)

fruits.sort() # ordena a lista
print(fruits)