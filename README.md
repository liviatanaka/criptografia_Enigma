# criptografia_Enigma
APS 1 - Algebra Linear e Teoria da Informação - 2021.1

# Indice
1. [Introdução](#introdução)
2. [Integrantes do grupo](#integrantes-do-grupo)
3. [Funcionamento do Enigma](#funcionamento-do-enigma)
4. [Implementação](#implementação)
5. [Funções disponíveis](#funções-disponíveis)
6. [Equações implementadas](#equações-implementadas)
7. [Como rodar](#como-rodar)
8. [Como rodar o demo](#como-rodar-o-demo)

## Integrantes do grupo
* Isabelle da Silva Santos
* Livia Tanaka

Essa é uma biblioteca em Python que possibilita a criptografia e descriptografia de mensagens por meio do algoritmo Enigma. Ela foi criada com o intuito de atender à demanda da APS-2 da disciplina de Álgebra Linear e Teoria da Informação, ministrada pelo professor Tiago Fernandes Tavares, no curso de Ciência da Computação do Insper.

## Funcionamento do Enigma
O algoritmo Enigma é uma cifra de substituição polialfabética que usa uma série de rotores para codificar letras em uma mensagem. Cada rotor é uma permutação dos caracteres do alfabeto, e a cifra é construída fazendo com que a mensagem passe pelos rotores em uma ordem específica.

A cifra Enigma é baseada em um conjunto de equações matemáticas que determinam como os caracteres da mensagem são substituídos. As equações que governam a criptografia e a decriptografia são altamente não lineares e complexas.

## Implementação
Esta biblioteca implementa a cifra Enigma usando matrizes de permutação para representar os rotores. A cifra é construída aplicando a matriz de permutação correspondente a cada rotor em ordem. A biblioteca também inclui funções para codificar mensagens como matrizes usando one-hot encoding, bem como funções para converter essas matrizes de volta em mensagens legíveis.

## Funções disponíveis
* `para_one_hot(msg)`: Transforma a mensagem em matriz usando one-hot encoding.
* `para_string(M)`: Converte uma matriz one-hot encoding em uma string legível.
* `cifrar(msg, P)`: Aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada.
* `de_cifrar(msg, P)`: Recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original.
* `enigma(msg, P, E)`: Faz a cifra Enigma na mensagem de entrada usando o cifrador P e o cifrador auxiliar E.
* `de_enigma(msg, P, E)`: Recupera uma mensagem cifrada como Enigma assumindo que ela foi cifrada com o usando o cifrador * P e o cifrador auxiliar E.

## Equações implementadas
Para cifrar uma mensagem usando Enigma, a matriz de permutação de cada rotor é aplicada à mensagem em ordem. Isso é feito da seguinte maneira:

### Criptografia
A criptografia com Enigma envolve uma série de operações realizadas em uma mensagem de texto, incluindo permutações e substituições de letras. A implementação deste repositório utiliza duas matrizes de permutação, P e E, para realizar a cifra Enigma.

A função enigma recebe como entrada uma mensagem de texto, a matriz P e a matriz E, e retorna a mensagem cifrada. Para cada letra da mensagem, a função realiza as seguintes operações:

1. Transforma a letra em uma matriz one-hot encoding.
2. Multiplica a matriz da letra pela matriz de permutação P.
3. Concatena a matriz resultante à matriz final da mensagem cifrada.
4. Multiplica a matriz de permutação P pela matriz E.

Ao final das operações, a função retorna a mensagem cifrada em texto.

### Decriptografia
A decriptografia com Enigma segue o mesmo processo da criptografia, porém com a ordem das matrizes de permutação invertida. A função de_enigma recebe como entrada uma mensagem cifrada, a matriz P e a matriz E, e retorna a mensagem original. Para cada letra da mensagem cifrada, a função realiza as seguintes operações:

1. Transforma a letra cifrada em uma matriz one-hot encoding.
2. Multiplica a matriz da letra pela matriz inversa de P.
3. Concatena a matriz resultante à matriz final da mensagem 4.original.
4. Multiplica a matriz de permutação P pela matriz E.

Ao final das operações, a função retorna a mensagem original em texto.

### Funções auxiliares

As funções auxiliares para a biblioteca de criptografia enigma incluem `limpa_mensagem`, que transforma uma mensagem em minúsculas, remove acentos e substitui caracteres especiais por "_", e `cria_matriz`, que recebe uma chave, realiza uma rotação e cria uma matriz de codificação usando o novo alfabeto.

## Como rodar

Para rodar o demo da biblioteca Enigma, siga as instruções abaixo:

1. Certifique-se de que o Python 3.6 ou superior está instalado no seu computador.
2. Clone ou faça o download do repositório no seu computador.
3. Acesse a pasta raiz do projeto no terminal.
4. Instale as dependências da biblioteca com o comando:

    ```bash
    pip install -r requirements.txt
    ```
5. Certifique-se de que as bibliotecas unidecode, flask, flask_restful, requests e numpy estejam instaladas no seu ambiente virtual. Para instalar essas bibliotecas, você pode usar o gerenciador de pacotes pip. Abra um terminal ou prompt de comando e execute o seguinte comando:
    
        ```bash
        pip install unidecode flask flask_restful requests numpy
        ```
## Como rodar o demo
1. Em seguida, execute o seguinte comando no terminal:  

    ```bash
    python demo.py
    ```

Isso iniciará o servidor Flask e o demo estará disponível no endereço http://localhost:5000.

Para usar a biblioteca em outro projeto, siga as seguintes instruções:

2. Importe a biblioteca Enigma no seu arquivo Python:
    
        ```python
        from enigmalille import *
        ```

## Como usar a biblioteca

* Mensagens normais: 
* Mensagens com caracteres que não fazem parte do alfabeto: 
* Mensagens vazias: 