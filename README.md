# Problema do Robô #

Considere um robô programado para coletar latas jogadas no chão. Nessa versão simplificada, o mundo é representado por uma malha quadricular 2D (duas dimensões), sendo que todos os objetos (robô e latas) ocupam apenas uma célula da malha. O objetivo é minimizar o número de passos que o robô deve fazer para coletar todas as malhas disponíveis.

## Requisitos ##

* As latas ocupam 20% de toda a malha.
* As paredes (limites da malha) não podem ser atravessadas.
* Não se pode refazer um movimento, e.g: esquerda-direita, cima-baixo...

## Algoritmo Evolutivo ##

Para a solução desse problema será desenhado um algoritmo genético com estrutura geracional, ou seja, a população seguinte é sempre substituida por uma nova, baseado nos processos de seleção, reprodução e mutação. Além disso, para não termos problemas de otimização também foi aplicada uma taxa de elitismo, para sempre preservar ao menos uma pequena parcela dos melhores indivíduos.

### Ambiente ###

O ambiente aqui é dado pela malha bidimensional de tamanho variável (aqui será usado valores de 10x10, 20x20 e 50x50). Essa malha é uma matriz NxN onde cada campo possui o seu respectivo X e Y. O robô sempre inicia na posição (0, 0) e as latas são aleatóriamente distribuidas por toda a matriz.

```
[ 2  1  0  0  1  0  0  0  0  0 ]
[ 0  1  0  0  0  0  1  0  0  0 ]
[ 0  0  0  0  0  0  0  0  1  1 ]
[ 0  0  0  0  0  1  0  0  0  0 ]
[ 0  0  0  0  0  0  1  0  0  0 ]
[ 0  0  0  0  0  1  1  1  0  0 ]
[ 0  0  0  0  0  0  0  1  0  0 ]
[ 1  1  0  0  1  0  0  0  0  0 ]
[ 0  1  0  0  0  1  1  0  0  1 ]
[ 1  0  0  0  0  0  0  0  0  0 ]
```

Esse é um exemplo de uma malha 10x10, "2" representa o robô, "1" representa uma latinha e "0" representa espaço vazio.

### Cromossomo ###

Com essa perspectiva do ambiente, as latas são enumeradas da esquerda para a direita e de cima para baixo, sendo iniciadas com o índice 0. No exemplo acima temos uma matriz 10x10 contendo 20 latas, ou seja, a enumeração será de 0 até 19, associando as latas com o campo acima temos o seguinte:

```
[(0, 1), (0, 4), (1, 1), (1, 6), (2, 8), (2, 9), (3, 5), (4, 6), (5, 5), (5, 6), (5, 7), (6, 7), (7, 0), (7, 1), (7, 4), (8, 1), (8, 5), (8, 6), (8, 9), (9, 0)]
```

Dessa forma, o cromossomo é uma representação da ordem que as latinhas serão pegadas, baseada no índice de cada uma. Nesse caso em específico será um array contendo valores de 0 a 19 distribuidos aleatoriamente, por exemplo:

```
[5, 0, 2, 1, 4, 8, 10, 11, 13, 12, 15, 19, 18, 17, 16, 14, 7, 9, 6, 3]
```

Logo, ainda nesse exemplo em questão, o caminho que o robô iria percorrer seria

```
[(2, 9), (0, 1), (1, 1), (0, 4), (2, 8), (5, 5), (5, 7), (6, 7), (7, 1), (7, 0), (8, 1), (9, 0), (8, 9), (8, 6), (8, 5), (7, 4), (4, 6), (5, 6), (3, 5), (1, 6)]
```

#### Decodificação ####

Esse final representa a ordem que o robô irá coletar as latas, porém ainda não é um passo a passo e ainda não é possível avaliar a distância total percorrida, assim ainda precisamos decodifica-lo. Essa decodificação será feita integralmente dentro de `available.py`, e detalhes da implementação são melhores visto por lá.

A princípio o robô segue uma ordem de prioridade que é mutável a longo do tempo, essa ordem define se o robô primeiro segue movimentos verticais ou horizontais, ou então, em casos especificos se deve ir para direita ou esquerda. Para evitar que o robô passe por uma lata sem querer, antes de pegar outra, essas soluções serão tratadas, pois caso contrário poderiamos ter uma deficiência na otimização do algoritmo.

Vamos continuar com o exemplo da matriz e do cromossomo acima, dessa forma começar a calcular a distância para esse cromossomo em questão

```
[(2, 9), (0, 1), (1, 1), (0, 4), (2, 8), (5, 5), (5, 7), (6, 7), (7, 1), (7, 0), (8, 1), (9, 0), (8, 9), (8, 6), (8, 5), (7, 4), (4, 6), (5, 6), (3, 5), (1, 6)]
```

Primeiro o robô vai partir da posição (0, 0) e deve chegar até (2, 9). Se o robô estiver com prioridade horizontal, antes de chegar no objetivo ele irá passar por duas latas: (0, 1) e (0, 4). Se o robô estiver com prioridade vertical ele antes irá passar pela lata (2, 8). Independente de qual caminho o robô optar por escolher, todo o passo a passo será armazenado em um array de caminhos e o cromossomo será consertado (informando que passou por outras latas primeiro). Seguindo de início a posição horizontal, o caminho que será armazenado será:

```
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [1, 9], [2, 9]]
```

Assim o robô já fez 12 passos e coletou um total de três latinhas. Todo esse passo a passo será seguido até que não sobre nenhuma latinha na malha. Ao final teremos um array informando todo o caminho que o robô seguiu, e a partir dele extraimos a distâncial total.

### Função Objetivo ###

Calculando a distância percorrida no tópico anterior é possível entender como funciona a função objetivo nesse caso, ela deve ser minimizada, de forma que priorize sempre soluções que tenham coletado todas as latas em uma quantidade menor de passos.

### Crossover ###

O crossover ou a recombinação optada nesse caso foi de primeira ordem "OX". Essa escolha se deve por tratar possíveis soluções inválidas, nesse caso seria a repetição de genes ou genes faltantes.

![Crossover example](https://github.com/Alisson2k/robot-problem-solves/raw/master/docs/crossover.png)
*Fonte https://www.youtube.com/watch?v=HATPHZ6P7c4&ab_channel=NoureddinSadawi*

Aqui são selecionados dois cromossomos para aplicar o cruzamento, nesse caso `[1, 2, 3, 4, 5, 6, 7, 8, 9]` e `[9, 3, 7, 8, 2, 6, 5, 1, 4]`. A principío é feito um corte no primeiro e todos os genes nesse ponto é posto no filho, exatamente na mesma posição. Depois disso o filho começa a ser preenchido com os valores do segundo cromossomo, começando a partir do primeiro gene a direita do ponto de corte, caso um gene do segundo já esteja preenchido no filho, esse gene é ignorado e passa para o próximo. Esse processo é feito até que o cromossomo têm todos os seus genes preenchidos, gerando assim um novo indivíduo.

### Mutação ###

Foram desenhadas duas mutações distintas, sendo a reversa e aleatória, e seu objetivo é muito simples, a ideia aqui é alterar completamente a estrutura do cromossomo, para dessa forma evitar quaisquer mínimos locais. Os melhores resultados aqui foram todos obtidos com a mutação reversa, e por isso ela foi a escolhida.

#### Mutação Reversa ####

Os genes do cromossomos são completamente invertidos. Exemplo:

**Antes da mutação:**

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

**Depois da mutação:**
```
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

#### Mutação Aleatória ####

Os genes dos cromossomos são completamente recombinados. Exemplo:

**Antes da mutação:**

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
```

**Depois da mutação:**
```
[8, 7, 11, 14, 13, 9, 19, 6, 17, 0, 3, 16, 10, 4, 1, 18, 12, 5, 15, 2]
```

### Resultados ###

Fora do algoritmo foram organizado testes com outros tipos de crossover, em especial PMX e CX, como ambos iriam ocasionar soluções inválidas das quais seriam necessarias tratar, optamos por manter apenas o OX, que inclusive obtiveram soluções ótimas. As tabelas abaixo mostram os testes com diferentes tamanhos de matrizes, sendo 10x10, 20x20 e 50x50. Outros testes também foram feitos, porém não obtivemos bons resultados, a tabela é um filtro dos melhores resultados para cada tamanho de geração testado.

#### Matriz 10x10 ####

|   | Tamanho população | Quantidade gerações | Chance de mutação | Taxa de elitismo | Menor distância | Média |
|---|:-----------------:|:-------------------:|:-----------------:|:----------------:|:---------------:|-------|
| 1 |         20        |         500         |         5%        |        20%       |        39       |       |
| 2 |         20        |         500         |         5%        |        20%       |        44       |       |
| 3 |         20        |         500         |         5%        |        20%       |        45       |   43  |
| 4 |         30        |         1000        |         7%        |        25%       |        52       |       |
| 5 |         30        |         1000        |         7%        |        25%       |        48       |       |
| 6 |         30        |         1000        |         7%        |        25%       |        45       |   48  |
| 7 |         50        |         1500        |        10%        |        15%       |        42       |       |
| 8 |         50        |         1500        |        10%        |        15%       |        43       |       |
| 9 |         50        |         1500        |        10%        |        15%       |        43       |   43  |

#### Matriz 20x20 ####

|   | Tamanho população | Quantidade gerações | Chance de mutação | Taxa de elitismo | Menor distância | Média |
|---|:-----------------:|:-------------------:|:-----------------:|:----------------:|:---------------:|-------|
| 1 |         20        |         100         |         5%        |        15%       |       272       |       |
| 2 |         20        |         100         |         5%        |        15%       |       270       |       |
| 3 |         20        |         100         |         5%        |        15%       |       287       |  276  |
| 4 |         30        |         300         |         7%        |        20%       |       252       |       |
| 5 |         30        |         300         |         7%        |        20%       |       234       |       |
| 6 |         30        |         300         |         7%        |        20%       |       241       |  242  |
| 7 |         50        |         500         |        10%        |        25%       |       235       |       |
| 8 |         50        |         500         |        10%        |        25%       |       214       |       |
| 9 |         50        |         500         |        10%        |        25%       |       209       |  219  |

#### Matriz 50x50 ####

|   | Tamanho população | Quantidade gerações | Chance de mutação | Taxa de elitismo | Menor distância | Média |
|---|:-----------------:|:-------------------:|:-----------------:|:----------------:|:---------------:|-------|
| 1 |         20        |          50         |         5%        |        15%       |       2780      |       |
| 2 |         20        |          50         |         5%        |        15%       |       2670      |       |
| 3 |         20        |          50         |         5%        |        15%       |       2875      |  2775 |
| 4 |         30        |         100         |         7%        |        20%       |       2501      |       |
| 5 |         30        |         100         |         7%        |        20%       |       2519      |       |
| 6 |         30        |         100         |         7%        |        20%       |       2504      |  2508 |
| 7 |         50        |         150         |        10%        |        25%       |       2468      |       |
| 8 |         50        |         150         |        10%        |        25%       |       2471      |       |
| 9 |         50        |         150         |        10%        |        25%       |       2489      |  2476 |

### Como rodar ###

O projeto não leva nenhuma biblioteca externa do python, portanto não é preciso fazer nenhuma instalação a mais.

Utilizando python3.6+, rode:

```
python main.py
```

Caso desejar, pode alterar quaisquer valores para obter diferentes resultados, ainda dentro de `main.py`:

```py
# Tamanho do problema
MATRIX_SIZE = 10

# Tamanho da população
POPULATION_SIZE = 20

# Quantidade de gerações
NUMBER_OF_GENERATIONS = 500

# Chance de mutação
MUTATION_RATE = 10

# Taxa de elitismo
ELITISM_RATE = 25
```
