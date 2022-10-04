#Escrevendo os primeiros arquivos

#Antes de escrever nosso primeiro arquivo, precisamos saber que todo arquivo com extensão .py é considerado um módulo.

#Módulos são declarados utilizando snake case, ou seja, com nomes minúsculos e quando possuírem mais de uma palavra, devem ser separadas por underscore (_).

PI = 3.14  # PI é uma "constante" em nosso módulo


def square(side):
    '''Calculate area of square.'''
    return side * side


def rectangle(length, width):
    '''Calculate area of rectangle.'''
    return length * width


def circle(radius):
    '''Calculate area of circle.'''
    return PI * radius * radius

#Observe que esse código segue algumas boas práticas para legibilidade, tais como:

#Entre cada função temos um espaço de 2 linhas;

#As funções são declaradas com nomes em letras minúsculas;

#A constante PI é definida em letras maiúsculas.

#⚠️Aviso: Existe uma convenção de declarar valores considerados constantes com letras maiúsculas, e o respeito #por outros programadores de não alterarem aquele valor.

#Hora de testá-lo! No fim do arquivo, vamos adicionar algumas linhas para imprimir a área de algumas figuras geométricas.

# ...

#Para corrigir, podemos acrescentar uma condicional ao módulo para somente exibir esses valores de teste quando o módulo for executado como script.

#A variável __name__ é utilizada pelo interpretador Python para identificar o arquivo que esta sendo executado e seu valor será "__main__" quando invocamos um módulo como scri

if __name__ == "__main__":
    print("Área do quadrado:", square(10))
    print("Área do retângulo:", rectangle(2, 2))
    print("Área do círculo:", circle(3))