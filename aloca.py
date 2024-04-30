

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

def aloca_navios(m, b):
    tam = len(m)
    linha = random.randint(0, n-1)
    coluna = random.randint(0, n-1)
    orientacao = random.choice(['h', 'v'])
    for i in b:
        pode_alocar = posicao_suporta(m,b,l,c,orient_aloc)
        while pode_alocar == False:
            linha = random.randint(0, n-1)
            coluna = random.randint(0, n-1)
            orientacao = random.choice(['h', 'v'])
            pode_alocar = posicao_suporta(m,b,l,c,orient_aloc)
            

