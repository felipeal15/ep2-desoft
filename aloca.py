

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
import random

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
