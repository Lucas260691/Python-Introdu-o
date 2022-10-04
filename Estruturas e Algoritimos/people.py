#Vamos utilizar o nosso módulo de calcular área de figuras planas. Escreva um novo arquivo com nome people.py e ele será um script para calcular pessoas que estão presentes em um show, dado a área do mesmo.

import area


PEOPLE_PER_SQUARE_METER = 2  # numero de pessoas por metro quadrado em média
FIELD_LENGTH = 60  # em metros
FIELD_WIDTH = 45  # em metros
people_at_concert = (
    area.rectangle(FIELD_LENGTH, FIELD_WIDTH) * PEOPLE_PER_SQUARE_METER
)
print("Estão presentes no show aproximadamente", people_at_concert, "pessoas.")

#Anota aí ✏️: O import é utilizado para termos todas as funções do módulo disponíveis em outro arquivo. Uma outra maneira de utilizarmos é escrevendo from area import rectangle, por exemplo, se quisermos importar apenas rectangle a partir de area. Porém, tome cuidado com conflitos de nomes caso use essa segunda maneira.

#Ao executá-lo com o comando python3 people.py, vemos que a saída não foi bem como esperávamos.

#Os nossos valores de teste estão sendo exibidos quando importamos o módulo. Mas não queremos que isso aconteça.

#Para corrigir, podemos acrescentar uma condicional ao módulo para somente exibir esses valores de teste quando o módulo for executado como script.
