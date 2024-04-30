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