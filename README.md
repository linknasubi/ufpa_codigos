# Repositório Com Objetivo de Armazenar Os Trabalhos Desenvolvidos No Decorrer Do Curso De Ciência Da Computação Na Universidade Federal Do Pará (UFPA)

## Trabalhos De Destaque

* [Representação Visual Em Algoritmos De Busca](#representação-visual-em-algoritmos-de-busca)
* [Site Lúdico Para A Disciplina De Psicologia](#site-lúdico-para-a-disciplina-de-psicologia)

## Representação Visual Em Algoritmos De Busca

A partir dos conhecimentos adquiridos na disciplina de Grafos, foi elaborada uma representação visual dos algoritmos de busca DFS e BFS, no qual é possível modificar de maneira
livre relações entre grafos, seja através de grafos direcionados, não direcionados, modificar o número de nós e gerir suas respectivas ligações.

### DFS
![](https://media4.giphy.com/media/aFbPDE7wLaaOBeLnsW/giphy.gif)

### BFS
![](https://media1.giphy.com/media/7uiYYd40IJTpPUiUhW/giphy.gif)

### Técnicas

#### Tecnologia

A principal tecnologia utilizada foi a API presente nos elementos do HTML, Canvas JS.


#### Surgimento Aleatório de Nós

O Container do Canvas é dividido em diversos quadrantes, correspondentes ao dobro do número de nós existentes no grafo em questão, uma vez associado a cada quadrante uma posição,
largura e altura, esse por sua vez é adicionado a um conjunto contendo todos quadrantes, os quais, uma vez selecionados para abrigar um nó serão removidos do conjunto de quadrantes.

O primeiro nó surge próximo ao centro do Container Canvas, a partir de uma relação probabilística, em seguida, todos nós adjacentes ao primeiro surgirão a uma distância de, no máximo, dois quadrantes
do nó adjacente anterior, continuando o posicionamento até que todos os nós tenham, efetivamente, ocupado seu devido espaço.


#### Algoritmos De Busca

O DFS foi implementado de maneira recursiva, enquanto o BFS de maneira iterativa.


## Site Lúdico Para A Disciplina De Psicologia

A partir dos assuntos abordados no desenvolvimento da disciplina de Psicologia para Computação, foi desenvolvido em um conjunto de 5 integrantes um site com propósitos lúdicos visando um público infantil.

### Contribuição Pessoal

Trabalhando no que compete ao JavaScript no site - excluso o código já existente em frameworks importados durante o projeto, como o Bootstrap - elaborei o sistema de jogo utilizando a ferramenta exclusivamente a ferramenta do Canvas JS.

![](https://media1.giphy.com/media/BxKijrlbP43vsv60rP/giphy.gif)
![](https://imgur.com/undefined)
