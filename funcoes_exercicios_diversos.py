# -*- coding: utf-8 -*-
"""funcoes-exercicios_diversos

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I9GtliGhH3o1caf92YVgg_cr6EpDXMYk

Crie a função
def taboada(n):
171 17
Apresenta a taboada do inteiro n,
onde 1 <= n <= 9.
que reproduz a taboada do número n na forma (exemplo para n = 7):
"""

def taboada(n):
    if n < 1 or n > 9:
        print("Número fora do intervalo permitido (1 a 9).")
        return
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Exemplo de uso:
taboada(9)

""" Implemente uma função que receba um valor n inteiro e imprima até a n-ésima linha da seguinte forma:
1
2 2
3
3 3
:
..
:
nnnnnn... n
Show code

"""

def imprimir_padrao(n):
    for i in range(1, n + 1):
        # Imprime os números de 1 até i
        for j in range(1, i + 1):
            print(i, end=" ")
        print()  # Imprime uma nova linha após cada linha de números

# Exemplo de uso:
imprimir_padrao(5)

"""(3) Implemente uma função que receba um valor n inteiro e imprima até a n-ésima linha da seguinte forma:
1
1 2
1 2 3

"""

def imprimir_linhas(n):
    # Definindo uma função chamada imprimir_linhas que recebe um argumento inteiro n
    for i in range(1, n + 1):
        # Iniciando um loop que vai de 1 até n (inclusive)
        linha = ""
        # Inicializando uma string vazia chamada linha
        for j in range(1, i + 1):
            # Iniciando um loop que vai de 1 até o valor atual de i (inclusive)
            linha += str(j) + " "
            # Adicionando o número atual j à string linha, convertendo-o para string e acrescentando um espaço
        print(linha)
        # Imprimindo a linha atual

# Exemplo de uso
n = int(input("Digite o valor de n: "))
# Solicitando ao usuário que insira o valor de n e convertendo-o para inteiro
imprimir_linhas(n)
# Chamando a função imprimir_linhas com o valor inserido pelo usuário como argumento

"""Implemente uma função que receba um valor em segundos e imprima o correspondente em horas, minutos e segundos. Por exemplo, se a função receber como argumento 4814, imprimirá 1 hora(s) 20 minuto(s) e 14 segundo(s)."""

def segundos_para_tempo(total_segundos):
    # Calcula o número de horas dividindo o total de segundos por 3600
    horas = total_segundos // 3600

    # Calcula o número de minutos restantes dividindo o resto da divisão dos segundos por 3600 por 60
    minutos = (total_segundos % 3600) // 60

    # Calcula o número de segundos restantes dividindo o total de segundos por 60
    segundos = total_segundos % 60

    # Imprime o resultado
    print(f"{horas} hora(s) {minutos} minuto(s) e {segundos} segundo(s)")

# Exemplo de uso
segundos_para_tempo(4814)

def segundos_para_tempo(total_segundos):
    # A função divmod() retorna o quociente e o resto da divisão
    # total_segundos dividido por 3600 (para obter as horas)
    horas, resto = divmod(total_segundos, 3600)

    # Em seguida, usamos novamente a função divmod() para calcular
    # os minutos e segundos a partir do resto obtido anteriormente
    minutos, segundos = divmod(resto, 60)

    # Imprime o resultado formatado com o número de horas, minutos e segundos
    print(f"{horas} hora(s) {minutos} minuto(s) e {segundos} segundo(s)")

# Exemplo de uso
segundos_para_tempo(4814)

"""Implemente uma função que retorna True se o argumento de entrada for um número natural primo e False caso contrário."""

def eh_primo(numero):
    # Verifica se o número é menor ou igual a 1, pois números menores ou iguais a 1 não são primos
    if numero <= 1:
        return False

    # Percorre todos os números de 2 até a raiz quadrada do número + 1
    for i in range(2, int(numero ** 0.5) + 1):
        # Se o número for divisível por algum número dentro deste intervalo, então não é primo
        if numero % i == 0:
            return False

    # Se nenhum divisor foi encontrado, o número é primo
    return True

# Exemplos de uso
print(eh_primo(7))  # True
print(eh_primo(10)) # False

def eh_primo(numero):
    # Verifica se o número é menor ou igual a 1
    if numero <= 1:
        return False

    # Percorre todos os números de 2 até o próprio número - 1
    for i in range(2, numero):
        # Se encontrar algum divisor, o número não é primo
        if numero % i == 0:
            return False

    # Se nenhum divisor foi encontrado, o número é primo
    return True

# Exemplos de uso
print(eh_primo(7))  # True
print(eh_primo(10)) # False

"""(6) Implemente uma função que retorne a quantidade de dígitos de um determinado número natural passado como argumento. Por exemplo, ao chamar a função com o número 2131, ela
deverá retornar 4.
"""

def contar_digitos(numero):
    # Converte o número para uma string e depois calcula o comprimento da string
    return len(str(numero))

# Exemplo de uso
print(contar_digitos(2131))  # Saída: 4

def contar_digitos(numero):
    # Inicializa o contador de dígitos como 0
    contador = 0

    # Enquanto o número for maior que 0
    while numero > 0:
        # Incrementa o contador de dígitos
        contador += 1
        # Remove o último dígito do número dividindo por 10 e arredondando para baixo
        numero //= 10

    # Retorna o contador de dígitos
    return contador

# Exemplo de uso
print(contar_digitos(2131))  # Saída: 4

"""(7) Implemente a função todos_iguais (sequencia) que retorna True se todos os elementos de sequencia forem iguais, e retorna False caso contrário."""

def todos_iguais(sequencia):
    # Verifica se todos os elementos da sequência são iguais ao primeiro elemento
    return all(elemento == sequencia[0] for elemento in sequencia)

# Exemplo de uso
print(todos_iguais([1, 1, 1, 1]))  # Saída: True
print(todos_iguais([1, 2, 1, 1]))  # Saída: False

def todos_iguais(sequencia):
    # Retorna True se todos os elementos forem iguais ao primeiro elemento da sequência
    return sequencia.count(sequencia[0]) == len(sequencia)

# Exemplo de uso
print(todos_iguais([1, 1, 1, 1]))  # Saída: True
print(todos_iguais([1, 2, 1, 1]))  # Saída: False

"""
(8) Implemente a função todos_diferentes (sequencia) que retorna True se todos os
elementos de sequencia forem diferentes entre si, e retorna False caso contrário, isto é, pelos
menos um elemento seja igual a outro componente da sequencia."""

def todos_diferentes(sequencia):
    # Cria um dicionário vazio para armazenar os elementos da sequência como chaves
    # e o número de ocorrências de cada elemento como valores
    elementos = {}

    # Percorre a sequência
    for elemento in sequencia:
        # Verifica se o elemento já está no dicionário
        if elemento in elementos:
            # Se o elemento já existir no dicionário, significa que há uma duplicata
            return False
        else:
            # Se o elemento não existir no dicionário, adiciona-o com valor 1
            elementos[elemento] = 1

    # Se nenhum elemento repetido for encontrado, retorna True
    return True

# Exemplo de uso:
print(todos_diferentes([1, 2, 3, 4, 5]))  # True
print(todos_diferentes([1, 2, 3, 4, 4]))  # False

def todos_diferentes(sequencia):
    # Percorre a sequência
    for i in range(len(sequencia)):
        # Para cada elemento, verifica se ele é igual a algum outro elemento da sequência
        for j in range(i+1, len(sequencia)):
            if sequencia[i] == sequencia[j]:
                # Se encontrar dois elementos iguais, retorna False
                return False
    # Se nenhum par de elementos iguais for encontrado, retorna True
    return True

# Exemplo de uso:
print(todos_diferentes([1, 2, 3, 4, 5]))  # True
print(todos_diferentes([1, 2, 3, 4, 4]))  # False

def todos_diferentes(sequencia):
    # Se o comprimento do conjunto formado a partir da sequência for igual ao comprimento da sequência original,
    # significa que todos os elementos são diferentes entre si, então retornamos True.
    # Caso contrário, pelo menos um elemento se repete, então retornamos False.
    return len(set(sequencia)) == len(sequencia)

# Exemplo de uso:
print(todos_diferentes([1, 2, 3, 4, 5]))  # True
print(todos_diferentes([1, 2, 3, 4, 4]))  # False

def todos_diferentes(sequencia):
    # Converte a sequência em um conjunto.
    # Um conjunto é uma coleção não ordenada de elementos únicos.
    # Qualquer duplicata na sequência será removida.
    conjunto = set(sequencia)

    # Compara o tamanho do conjunto com o tamanho da sequência original.
    # Se forem iguais, significa que todos os elementos são diferentes entre si.
    # Caso contrário, pelo menos um elemento se repete.
    return len(conjunto) == len(sequencia)

# Exemplo de uso:
print(todos_diferentes([1, 2, 3, 4, 5]))  # True
print(todos_diferentes([1, 2, 3, 4, 4]))  # False

"""(9) Implemente uma função que recebe como argumentos um número n e uma lista de números, indice_elemento(n, lista). A função retornará o índice da primeira ocorrênia do
número na lista e -1 se o número não estiver na lista. Obs: em Python, índices de listas, arrays,
etc. começam em 0.
"""

def indice_elemento(n, lista):
    # Percorre a lista
    for i in range(len(lista)):
        # Verifica se o elemento atual é igual ao número desejado
        if lista[i] == n:
            # Se encontrar, retorna o índice
            return i
    # Se o número não estiver na lista, retorna -1
    return -1

# Exemplo de uso:
print(indice_elemento(3, [1, 2, 3, 4, 5]))  # Saída: 2 (o índice do número 3 é 2)
print(indice_elemento(6, [1, 2, 3, 4, 5]))  # Saída: -1 (o número 6 não está na lista)

def indice_elemento(n, lista):
    try:
        # Retorna o índice da primeira ocorrência de n na lista
        return lista.index(n)
    except ValueError:
        # Se o número não estiver na lista, retorna -1
        return -1

# Exemplo de uso:
print(indice_elemento(3, [1, 2, 3, 4, 5]))  # Saída: 2 (o índice do número 3 é 2)
print(indice_elemento(6, [1, 2, 3, 4, 5]))  # Saída: -1 (o número 6 não está na lista)

"""(10) Implemente uma função que recebe um número n e retorna a menor potência de 2 maior ou igual a n. Por exemplo, pot2 (14) retornará 16, pot2(42) retornará 64."""

def pot2(n):
    potencia = 1
    while potencia < n:
        potencia *= 2
    return potencia

# Exemplos de uso:
print(pot2(14))  # Saída: 16
print(pot2(42))  # Saída: 64

import math

def pot2(n):
    # Calcula o logaritmo base 2 de n
    log2_n = math.ceil(math.log2(n))
    # Retorna 2 elevado ao logaritmo base 2 de n
    return 2 ** log2_n

# Exemplos de uso:
print(pot2(14))  # Saída: 16
print(pot2(42))  # Saída: 64

def pot2(n):
    # Encontra o bit mais significativo de n
    msb = 1
    while msb < n:
        msb <<= 1

    return msb

# Exemplos de uso:
print(pot2(14))  # Saída: 16
print(pot2(42))  # Saída: 64

"""(11) Implemente uma funçao que dado um número natural maior do que 1, decomponha esse número em fatores primos. Por exemplo, se o argumento de entrada for 36, a saída deverá
ser [2, 2, 3, 3], porque 2 × 2 × 3 × 3 = 36.
"""

def fatores_primos(n):
    fatores = []
    divisor = 2
    while n > 1:
        # Verifica se o número é divisível pelo divisor atual
        while n % divisor == 0:
            # Se for, adiciona o divisor à lista de fatores e divide o número pelo divisor
            fatores.append(divisor)
            n //= divisor
        # Incrementa o divisor para o próximo número primo
        divisor += 1
    return fatores

# Exemplo de uso:
print(fatores_primos(36))  # Saída: [2, 2, 3, 3]

"""(12) Implemente a função maiorN(lista, N) que recebe uma lista de números quaisquer, um
valor N, 1 <= N <= len(lista), e retorna o Nésimo maior valor na lista de números. Por
exemplo, se N for 1, retorna o maior valor na lista, se N for 2, retorna o segundo maior valor na
lista, etc. Exemplo:
"""

def maiorN(lista, N):
    # Ordena a lista em ordem decrescente
    lista_ordenada = sorted(lista, reverse=True)
    # Retorna o N-ésimo maior valor na lista
    return lista_ordenada[N-1]

# Exemplo de utilização:
lista = [5, -1, 7, 0, -3, 9]
N = 2
print(f'Em {lista} o {N}o. maior valor é {maiorN(lista, N)}')

"""(13) Implemente uma função recursiva div(m, n) que recebe como argumentos dois números naturais m en e devolve o resultado da divisão inteira de m por n. Não pode recorrer às operações aritméticas de multiplicação, divisão inteira e resto da divisão inteira.
Show code
Digite o valor de m (dividendo): 7 Digite o valor de n (divisor): 2
A divisão inteira de 7 por 2 é: 3
"""

def div(m, n):
    # Caso base: quando o dividendo é menor que o divisor, a divisão inteira é 0
    if m < n:
        return 0
    # Caso recursivo: subtrai o divisor do dividendo até que o dividendo seja menor que o divisor
    return 1 + div(m - n, n)

# Solicita ao usuário os valores de m (dividendo) e n (divisor)
m = int(input("Digite o valor de m (dividendo): "))
n = int(input("Digite o valor de n (divisor): "))

# Chama a função div e imprime o resultado
print(f"A divisão inteira de {m} por {n} é: {div(m, n)}")

"""(14) Implemente uma função que recebe o seu peso e altura e retorna seu índice de massa
corporal, IMC. A função também deverá emitir a classificação, de acordo com a tabela abaixo:
CLASSIFICAÇÃO
IMC
MENOR QUE 18,5
MAGREZA
ENTRE 18,5 E 25,0 NORMAL
ENTRE 25,0 E 30,0 SOBREPESO
ENTRE 30,0 E 40,0 OBESIDADE
MAIOR QUE 40,0
OBESIDADE GRAVE
Dica:
Show code
IMC
=
peso altura2
, peso em kg, altura em m
peso, altura = 59, 1.64 imc (peso, altura)
IMC = 21.9
Classificação Normal
"""

def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Define a classificação com base no IMC calculado
    if imc < 18.5:
        classificacao = "Magreza"
    elif 18.5 <= imc < 25.0:
        classificacao = "Normal"
    elif 25.0 <= imc < 30.0:
        classificacao = "Sobrepeso"
    elif 30.0 <= imc < 40.0:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade Grave"

    return imc, classificacao

# Exemplo de utilização:
peso, altura = 59, 1.64
imc, classificacao = calcular_imc(peso, altura)
print(f"IMC: {imc:.1f}")
print(f"Classificação: {classificacao}")

def calcular_imc(peso, altura):
    # Calcula o IMC
    imc = peso / (altura ** 2)

    # Define a classificação com base no IMC calculado usando um dicionário
    classificacoes = {
        "Magreza": lambda imc: imc < 18.5,
        "Normal": lambda imc: 18.5 <= imc < 25.0,
        "Sobrepeso": lambda imc: 25.0 <= imc < 30.0,
        "Obesidade": lambda imc: 30.0 <= imc < 40.0,
        "Obesidade Grave": lambda imc: imc >= 40.0
    }

    for classificacao, condicao in classificacoes.items():
        if condicao(imc):
            return imc, classificacao

# Exemplo de utilização:
peso, altura = 59, 1.64
imc, classificacao = calcular_imc(peso, altura)
print(f"IMC: {imc:.1f}")
print("Classificação:", classificacao)

"""(15) Para calcular a raiz quadrada de um número N > 0 podemos aplicar a seguinte fórmula
iterativa:
1
N
Xn+1
X n +
2
Xn
onde în representa a raiz quadrada do número calculada na iteração n. As iterações terminam quando N − x × n < 10-9. Assuma 1 = 1 e implemente a função raiz(N,
―
1
show=False). Note o parâmetro padrão (default) show. Impemente a função de forma que apenas quando show=True todos os valores estimados da raiz quadrada sejam impressos. Quando show=False, ou for ausente na chamada da função, nada será impresso. Em ambos os casos, o valor estimado da raiz quadrada será retornado pela função. Exemplos de uso:
>>> print(raiz(5))
2.236067977499978
>>> print(raiz(5, True))
x_1
= 1.00000
x_2 = 3.00000
X_3 = 2.33333
x_4 = 2.23810
x_5 = 2.23607
2.236067977499978
>>> print(raiz(5, False))
2.236067977499978
"""

def raiz(N, show=False):  # Define a função raiz com dois parâmetros, N e show (show tem um valor padrão False)
    x_n = 1.0  # Inicializa o valor inicial da raiz como 1.0
    iterations = 0  # Inicializa o contador de iterações como 0

    if show:  # Se show for True
        print(f"x_1 = {x_n:.5f}")  # Imprime o valor inicial da raiz com 5 casas decimais

    while True:  # Inicia um loop infinito
        x_n1 = (x_n + N / x_n) / 2  # Calcula o próximo valor da raiz usando o método de Newton-Raphson
        iterations += 1  # Incrementa o contador de iterações

        if show:  # Se show for True
            print(f"x_{iterations+1} = {x_n1:.5f}")  # Imprime o próximo valor da raiz com 5 casas decimais

        if abs(N - x_n1 * x_n1) < 1e-9:  # Verifica se a diferença entre N e o quadrado do próximo valor da raiz é menor que 1e-9
            break  # Se for, sai do loop

        x_n = x_n1  # Atualiza o valor atual da raiz para o próximo valor

    return x_n1  # Retorna o valor final estimado da raiz

print(raiz(5))  # Chama a função raiz com N=5 e não mostra as iterações
print(raiz(5, True))  # Chama a função raiz com N=5 e mostra as iterações
print(raiz(5, False))  # Chama a função raiz com N=5 e não mostra as iterações