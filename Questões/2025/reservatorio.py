V, A, C = map(int, input().split()) # Recebe a vazão, abastecimento e capacidade do reservatório
N = int(input()) # Recebe o número de operações

agua = 0
vazamento = False # Identifica se houve um vazamento

for i in range(N): # Realiza N operações
    O = input().split() # Recebe a operação
    O[1] = int(O[1]) # Torna o tempo da operação um número inteiro

    if O[0] == "E": # Caso a operação seja de entrada
        agua += A * O[1] # Adiciona uma quantidade de água ao reservatório igual ao produto do abastecimento pelo tempo
    
    elif O[0] == "S": # Caso a operação seja de saída
        agua -= V * O[1] # Retira uma quantidade de água do reservatório igual ao produto da vazão pelo tempo
    
    if agua > C: # Determina se houve um vazamento no tanque ou não
        vazamento = True

    if agua < 0: # Impede que haja uma quantidade de água negativa
        agua = 0

if vazamento: # Caso tenha ocorrido um vazamento
    print("vazamento")

else:
    print(agua)