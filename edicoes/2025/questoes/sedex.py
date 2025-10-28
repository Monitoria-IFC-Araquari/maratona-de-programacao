a = int(input()) # Recebe o diâmetro da bola de boliche
ok = True # Variavel que indica se a bola cabe ou não

dimensoes = [int(b) for b in input().split()] # Recebe a altura largura e profundidade do espaço

for b in dimensoes:
    ok = ok  and (a <= b) # Caso todas as dimensões da bola caibam no espaço, ok se mantém True, caso não, ok se torna False
    
print("S" if ok else "N") # Caso ok seja True imprima S, caso ok seja False imprima N                     