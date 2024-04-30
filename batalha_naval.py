#import(s)
import random

#FUNÇÕES BASE (4)

#PRIMEIRA FUNÇÃO BASE - CRIA MATRIZ QUADRADA DE ESPAÇOS
def cria_mapa(n):
  l = [' ']*n
  matriz=[l]*n
  return matriz
#SEGUNDA FUNÇÃO BASE OBRIGATÓRIA - VERIFICA SE ACABOU OS N DA MATRIZ
def foi_derrotado(matriz):
    for i in matriz:
        for x in i:
            if x == 'N':
                return False
    return True
#TERCEIRA E QUARTA FUNÇÃO BASE OBRIGATÓRIA - NAVIO PODE SER ALOCADO NA POSIÇÃO? , e ALOCANDO OS NAVIOS PARA O COMP.
def posicao_suporta(m, b, l, c, orient_aloc):
    if orient_aloc == 'v':
        if l + b > len(m):
            return False
        for i in range(b):
            if m[l+i][c] != ' ':
                return False
    if orient_aloc == 'h':
        if c + b > len(m):
            return False
        for i in range(b):
            if m[l][c+i] != ' ':
                return False
    return True

def aloca_navios(m, l_b):
    tam = len(m)
    for tam_n in l_b:
        l = random.randint(0, tam-1)
        c = random.randint(0, tam-1)
        orient_aloc = random.choice(['h', 'v'])
        pode_alocar = posicao_suporta(m, tam_n, l, c, orient_aloc)
        while pode_alocar == False:
            l = random.randint(0, tam-1)
            c = random.randint(0, tam-1)
            orient_aloc = random.choice(['h', 'v'])
            pode_alocar = posicao_suporta(m, tam_n, l, c, orient_aloc)
        if orient_aloc == 'v':
            for i in range(l, l+tam_n):
                m[i][c] = 'N'
        elif orient_aloc == 'h':
            for j in range(c, c+tam_n):
                m[l][j] = 'N'
    return m
#

#FUNCAO DE ESCOLHA DAS NAÇÕES JUNTAMENTE COM AS FROTAS

def escolher_nacao(jogador):
    print(f"Jogador {jogador}, escolha sua nação:")
    print(f"1. Brasil ! " ,  " Com a frota de:" ,
'1 cruzador',
'2 torpedeiro',
'1 destroyer',
'1 couracado',
"1 porta-avioes", )
    print("2. França",
" 3 cruzador" ,
" 1 porta-avioes" , 
" 1 destroyer ", 
" 1 submarino" ,
" 1 couracado"

          )
    print("3. Austrália")
    print("4. Rússia")
    print("5. Japão")
    escolha = input(" Qual o número da nação da sua frota?: ")
    if escolha == '1':
        return "Brasil"
    elif escolha == '2':
        return "França"
    elif escolha == '3':
        return "Austrália"
    elif escolha == '4':
        return "Rússia"
    elif escolha == '5':
        return "Japão"
    else:
        print("Escolha inválida.")
        return escolher_nacao(jogador)

#ESTABELECENDO O VALOR DAS FROTAS PARA CADA NAÇÃO

def aloca_frota_por_nacao(nacao):
    frota = []
    if nacao == "Brasil":
        frota = [2, 3, 3, 5, 4, 5]
    elif nacao == "Franca":
        frota = [2, 2, 5, 3, 4, 4, 5]
    elif nacao == "Austrália":
        frota = [2, 2, 3, 4, 4, 4, 5]
    elif nacao == "Austrália":
        frota = [2, 3, 3, 4, 5, 5]
    elif nacao == "Russia":
        frota = [2, 2, 2, 3, 4, 5]
    return frota

#CONECTANDO O VALOR DAS FROTAS EM SI, COM O NOME DELAS PREVIAMENTE ESTABELECIDOS 
#ALÉM DISSO, TESTANDO O FUNCIONAMENTO INCIAL DO JOGO

#COMMIT DE TESTE PARA VER SE ESTA FUNCIONANDO
    #JOGO
nacao = (escolher_nacao(1))


