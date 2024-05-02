#import(s)
import random
from constantes import *

#FUNÇÕES BASE (4)

#PRIMEIRA FUNÇÃO BASE - CRIA MATRIZ QUADRADA DE ESPAÇOS
def cria_mapa(n):
    l = []
    for i in range(n):
        l.append([' ']*n)

    return l
#SEGUNDA FUNÇÃO BASE OBRIGATÓRIA - VERIFICA SE ACABOU OS N DA MATRIZ
def foi_derrotado(matriz):
    for i in matriz:
        for x in i:
            if x == 'N':
                return False
    return True
#TERCEIRA E QUARTA FUNÇÃO BASE OBRIGATÓRIA - NAVIO PODE SER ALOCADO NA POSIÇÃO? , e ALOCANDO OS NAVIOS PARA O COMP.
def posicao_suporta(matriz, b, l, c, orient_aloc):
    if orient_aloc == 'v':
        if l + b > len(matriz):
            return False
        for i in range(b):
            if matriz[l+i][c] != ' ':
                return False
    if orient_aloc == 'h':
        if c + b > len(matriz):
            return False
        for i in range(b):
            if matriz[l][c+i] != ' ':
                return False
    return True

def aloca_navios(matriz, l_b):
    tam = len(matriz)
    for tam_n in l_b:
        l = random.randint(0, tam-1)
        c = random.randint(0, tam-1)
        orient_aloc = random.choice(['h', 'v'])
        pode_alocar = posicao_suporta(matriz, tam_n, l, c, orient_aloc)
        while pode_alocar == False:
            l = random.randint(0, tam-1)
            c = random.randint(0, tam-1)
            orient_aloc = random.choice(['h', 'v'])
            pode_alocar = posicao_suporta(matriz, tam_n, l, c, orient_aloc)
        if orient_aloc == 'v':
            for i in range(l, l+tam_n):
                matriz[i][c] = 'N'
        elif orient_aloc == 'h':
            for j in range(c, c+tam_n):
                matriz[l][j] = 'N'
    return m
#

#FUNCAO DE ESCOLHA DAS NAÇÕES JUNTAMENTE COM AS FROTAS

#ESTABELECENDO O VALOR DAS FROTAS PARA CADA NAÇÃO

def escolher_nacao(jogador):
    print(f"Jogador {jogador}, escolha sua nação:")
    for i, pais in enumerate(PAISES, start=1):
        print(f"{i}. {pais}")
    escolha = input("Digite o número correspondente à sua escolha: ")
    try:
        escolha = int(escolha)
        if 1 <= escolha <= len(PAISES):
            return list(PAISES.keys())[escolha - 1]
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")
            return escolher_nacao(jogador)
    except ValueError:
        print("Escolha inválida. Por favor, digite um número.")
        return escolher_nacao(jogador)

#CONECTANDO O VALOR DAS FROTAS EM SI, COM O NOME DELAS PREVIAMENTE ESTABELECIDOS 
#ALÉM DISSO, TESTANDO O FUNCIONAMENTO INCIAL DO JOGO

def verifica_colisao(tabuleiro, linha, coluna, tamanho_navio, orientacao):
    if orientacao == 'h':
        if coluna + tamanho_navio > 10:  # Verifica se o navio está dentro dos limites do tabuleiro
            print("O navio está fora dos limites do tabuleiro na orientação horizontal.")
            return True

        for j in range(coluna, coluna + tamanho_navio):
            if tabuleiro[linha][j] != ' ':  # Verifica se há uma colisão na posição
                print("O navio colide com outro navio na posição", linha, j)
                return True

    else:  # Orientação vertical
        if linha + tamanho_navio > 10:  # Verifica se o navio está dentro dos limites do tabuleiro
            print("O navio está fora dos limites do tabuleiro na orientação vertical.")
            return True

        for i in range(linha, linha + tamanho_navio):
            if tabuleiro[i][coluna] != ' ':  # Verifica se há uma colisão na posição
                print("O navio colide com outro navio na posição", i, coluna)
                return True

    return False


def ataque_comp(tabuleiro):
    l_at = random.randit(0, len(tabuleiro)-1)
    n_at = random.randint(0, len(tabuleiro)-1)
    if tabuleiro[l_at][n_at] == ' ':
        print('Água')
        tabuleiro[l_at][n_at] = 'A'
        return tabuleiro
    elif tabuleiroc == 'N':
        print('No alvo')
        tabuleiro[l_at][n_at] = 'X'
        return tabuleiro
    else:
        return ataque_comp(tabuleiro)






def atacar(tabuleiro):
    x = True
    l_at = input('Digite a letra correspondente a linha do ataque (ex:C):').upper()
    if l_at not in ALFABETO or len(l_at) != 1:
        x = False
        print('Letra inválida')
    while x == False:
        print(l_at)
    
    n_at = input('Digite o número correspondente a coluna do ataque (ex:4):')
    if n_at > 10 or len(l_nt) != 1:
        x = False
        print('Número inválido')
    
    while x == False:
        print(l_nt)


        
    


def aloca_navios_jogador(tabuleiro, jogador, nacao):
    frota = PAISES[nacao]
    print(f"Jogador {jogador}, aloque seus navios do(a) {nacao} no tabuleiro.")

    for tipo_navio, quantidade in frota.items():
        tamanho_navio = CONFIGURACAO[tipo_navio]
        print(f"Aloque {quantidade} navio(s) de tipo {tipo_navio} (tamanho {tamanho_navio}):")

        for _ in range(quantidade):
            while True:
                posicao = input("Digite a posição inicial (por exemplo, A1) e a orientação (h para horizontal, v para vertical), separadas por espaço: ")
                posicao = posicao.split()

                if len(posicao) != 2:
                    print("Entrada inválida. Digite a posição inicial e a orientação separadas por espaço.")
                    continue

                posicao_inicial = posicao[0].upper()
                orientacao = posicao[1].lower()

                if len(posicao_inicial) < 2 or posicao_inicial[0] not in 'ABCDEFGHIJ' or not posicao_inicial[1:].isdigit():
                    print("Posição inicial inválida. Use uma letra para a coluna (de A a J) seguida de um número para a linha (de 1 a 10).")
                    continue

                if orientacao not in ['h', 'v']:
                    print("Orientação inválida. Use 'h' para horizontal ou 'v' para vertical.")
                    continue

                coluna = ord(posicao_inicial[0]) - ord('A')
                linha = int(posicao_inicial[1:]) - 1

                # Check for collisions and boundary violations
                if verifica_colisao(tabuleiro, linha, coluna, tamanho_navio, orientacao):
                    print("Posição inválida. O navio colide com outro navio ou está fora dos limites do tabuleiro.")
                    continue

                if orientacao == 'h':
                    # Place the ship horizontally
                    for j in range(coluna, coluna + tamanho_navio):
                        tabuleiro[linha][j] = 'N'
                else:  # orientacao == 'v'
                    # Place the ship vertically
                    for i in range(linha, linha + tamanho_navio):
                        tabuleiro[i][coluna] = 'N'

                break

    return tabuleiro
# Agora tente alocar os navios novamente e veja se o problema persiste.

#COMMIT DE TESTE PARA VER SE ESTA FUNCIONANDO
#JOGO, EFETIVAMENTE
nacao = (escolher_nacao(1))
#CHAMANDO AS FUNCOES PARA CRIAR OS MAPAS, DANDO O TAMANHO DELES 
criar_comp = cria_mapa (10)
criar_jog = cria_mapa (10)
#CHAMANDO A FUNCAO DE ALOCAR OS NAVIOS COM OS PARAMETROS
alocar = aloca_navios_jogador (criar_jog, 1 , nacao)
