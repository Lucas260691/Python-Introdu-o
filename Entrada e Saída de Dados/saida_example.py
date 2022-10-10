#Saída

#Como já visto, a função print — que já vem embutida na linguagem — é a principal função para imprimirmos um valor em “tela”. Normalmente esta função escreve na saída padrão do sistema operacional, mas veremos que é possível modificar este e outros comportamentos.

#Esta função recebe parâmetros de forma variável, ou seja, pode receber nenhum, um, dois ou n parâmetros durante sua invocação.

print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultados são", 6, 23, 42)  # saída: Os resultados são 6 23 42

#O separador padrão dos argumentos é um espaço em branco, que pode ser alterado.

print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana

#Além do separador, podemos também alterar o caractere de fim de linha que, por regra, é uma quebra de linha:

print("Em duas ")
print("linhas.")

#Saída:

#Em duas
#linhas.

#Alterando o padrão:


print("Na mesma", end=" ")
print("linha.")
#Saída:

#Na mesma linha.

#Já sabemos que erros podem acontecer e o sistema operacional normalmente espera que um programa escreva seus erros na saída de erros.

#Existe um parâmetro que nos permite modificar a saída padrão para a saída de erros:

import sys


err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr)


#💡 Em Python, podemos fazer interpolação de variáveis e expressões utilizando f-string. Adicionamos um f antes das aspas e o valor de saída entre chaves. Essa dica é importante, pois é a maneira mais eficiente de formatar strings.

x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 3 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos



