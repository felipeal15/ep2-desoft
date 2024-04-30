def foi_derrotado(matriz):
    for i in matriz:
        for x in i:
            if x == 'N':
                return False
    return True
