# Desafio Python

## Sobre o projeto

O programa serve para encontrar a melhor opção de transportadora, a partir de alguns parâmetros, são eles:

* Velocidade (a transportadora mais rápida)
* Custo (a transportadora mais barata)

## Para executar o programa:

    python3 main.py nome_do_arquivo.csv peso nome_da_cidade

* O *nome_do_arquivo*.csv é opcional, caso não seja passado por padrão utilizaremos o transportadoras.csv;

* O *peso* é obrigatório e deve ser digitado em kg;

* O *nome_da_cidade* é obrigatório e pode ser digitado de qualquer forma (seja em maiúsculo ou em minúsculo, mas com o espaçamento correto).

  ### Exemplo de uso

  	python3 main.py transportadoras.csv 2 curitiba
  	python3 main.py 2 são paulo
  	python3 main.py 150 rio de janeiro
  	python3 main.py 50 belo horizonTE

* Caso sejam digitados menos campos do que o necessário o programa informará para consultar esse arquivo **PROJECT.md**;

* Caso seja digitado um nome de arquivo que não existe o programa informará que o arquivo não existe;

* Caso seja digitado o nome de uma cidade que também não existe na base de dados o programa informará isso;

* Caso seja digitado um valor diferente de numérico para peso o programa informará que o valor digitado para o peso é inválido.

Foi notado que na base de dados a cidade **Rio de Janeiro** está escrita errada (**Rio de Janiero**).



# Hierarquia de arquivos

Para o desenvolvimento desse desafio e com o intuito de organização, foram criados 4 arquivos, são eles:

* main.py

* cheapest_module.py

* fastest_module.py

* utils_module

  

## main.py

No arquivo *main.py* está o core da nossa aplicação, ela é responsável por receber e tratar os argumentos passados via linha de comando, processar os dados do arquivo csv e quando necessário chamar os módulos associados a ela para a realização de cálculos para saber qual a transportadora mais rápida e/ou mais barata.



## utils_module.py

No arquivo *utils_module.py* estão as funções que são importantes em todos os módulos do projeto, como:

* Funções de conversão entre strings e ints;
* Funções para saber qual o index utilizado, evitando números mágicos no código (enums).



## cheapest_module.py

No arquivo *cheapest_module* estão as funções responsáveis para calcular qual a transportadora mais barata e também para imprimir na tela caso essa transportadora exista, nela são utilizadas três funções:

* **get_cheapest_carrier**: função responsável por iterar pela tabela de transportadoras e conferir se o custo de frete/kg é menor que o último já salvo e também conferir se a cidade que estou olhando é exatamente a cidade digitada pelo usuário.
* **print_cheapest_carrier**: função responsável por imprimir a opção mais barata para o usuário.
* **calculate_cheapest_carrier**: função responsável por chamar a *get_cheapest_carrier* e a *print_cheapest_carrier* quando necessário.

## fastest_module.py

No arquivo *fastest_module* estão as funções responsáveis para calcular qual a transportadora mais rápida e também para imprimir na tela caso essa transportadora exista, nela são utilizadas três funções:

* **get_fastest_carrier**: função responsável por iterar pela tabela de transportadoras e conferir se o tempo é menor que o último já salvo e também conferir se a cidade que estou olhando é exatamente a cidade digitada pelo usuário. Como acordado com **Gustavo**, caso exista mais de uma transportadora com o menor tempo possível, todas as opções válidas devem ser mostradas na tela.
* **print_fastest_carrier**: função responsável por imprimir a opção mais rápida para o usuário.
* **calculate_fastest_carrier**: função responsável por chamar a *get_fastest_carrier* e a *print_fastest_carrier* quando necessário.
