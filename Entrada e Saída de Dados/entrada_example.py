#Entrada

#Uma das maneiras que existem de receber valores em nossos programas é através da função input, que vem embutida na própria linguagem. Esta função está vinculada à entrada padrão do sistema operacional e tem como parâmetro opcional o prompt que, caso seja fornecido, exibirá a mensagem passada para ele em tela. O valor recebido através da função será do tipo texto (str):

input("Digite uma mensagem:")

#O programa permanece parado até que algum dado seja fornecido. Isto pode ser feito digitando algum conteúdo, teclando Enter, ou podemos também ter os dados redirecionados de um arquivo ou outra fonte. Veja um exemplo de um programa com entrada de dados fornecido pela pessoa usuária:

import random

random_number = random.randint(1, 10)  # escolhe um número aleatório entre 1 e 10
guess = ""

while guess != random_number:  # enquanto não adivinhar o número
    guess = int(input("Qual o seu palpite? "))  # pergunte a pessoa usuária um número

print("O número sorteado era: ", guess)

#💡 Fazemos uma conversão do palpite para um número inteiro, pois entrada de dados é sempre str.

#💡 Para rodar o exemplo acima, não crie um arquivo chamado random para inserir o código, pois o módulo que estamos importando se chama random e isso pode causar um erro! Lembre-se que, para rodar o código, você deve executar o comando python3 nome_do_arquivo.py no terminal.

#Outra maneira de recebermos valores externos na execução de nossos programas é utilizando o módulo sys. Quando executamos um script e adicionamos parâmetros, os mesmos estarão disponíveis através de uma variável chamada sys.argv, que é preenchida sem que precisemos fazer nada. Na prática, podemos escrever o conteúdo abaixo em um arquivo e passar alguns parâmetros ao executá-lo.

import sys


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)

#Podemos executar o código usando os parâmetros através do comando abaixo:
#python3 arquivo.py 2 4 "teste"

#A saída será:

#Received ->  arquivo.py
#Received ->  2
#Received ->  4
#Received ->  teste

