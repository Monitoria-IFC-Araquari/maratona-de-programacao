N = int(input()) # Captura o número de tempos que serão inseridos

def sort_by_point(e): # Realiza a ordenação pelo tempo
    return int(e[1])

placares = {} # Variavel que armazena a pontuação em suas devidas categorias

for i in range(N): # Percorre todas as entradas do usuario
    pontuacao = input().split()
    
    if not pontuacao[2] in placares: # Caso a categoria digitada não exista, adicione ela
        placares[pontuacao[2]] = []

    placares[pontuacao[2]].append(pontuacao[0:2]) # Adiciona a entrada do usuario nas pontuações

for categoria in placares: # Ordena as pontuações nas categorias por ordem decrescente e as imprime na tela
    placares[categoria].sort(reverse=True, key=sort_by_point)
    print(categoria)
    for ponto in placares[categoria]:
        print(f"{ponto[0]} {ponto[1]}")