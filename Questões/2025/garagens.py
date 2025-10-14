N, P = map(int, input().split()) # Recebe o número de vagas na garagem e o número de operaçãoes

garagens  = [0 for i in range(N)] # Gera uma lista com as vagas
velhice = [0 for i in range(N)] # Gera uma lista que calcula quanto tempo se passou desde o ultimo uso

for i in range(P):
    o = input().split() # Recebe a operação

    if o[0] == "G": # Caso seja a operação de guardar
        indx = velhice.index(max(velhice)) # Identifica a vaga que não é usada a mais tempo
        garagens[indx] = 1 # Armazena o caminhão nessa vaga
        velhice[indx] = 0 # Reinicioa o contador de velhice
    
    elif o[0] == "S": # Caso seja a operação de saída
        pos = int(o[1])-1 # Ajusta o valor passado para o formato da lsita
        if garagens[pos] != 0: # Caso não esteja vazia
            garagens[pos] = 0 # Remove o caminhão
    
    for i in range(len(garagens)): # Percorre todas as vagas 
        if not garagens[i]: # Caso a vaga não esteja ocupada
            velhice[i] += 1 # Aumenta sua velhice em um
    

print(*garagens) # Imprime todas as vagas em uma única linha