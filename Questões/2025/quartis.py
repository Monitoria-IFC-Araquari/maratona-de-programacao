N = int(input()) # Recebe a quantidade de números
[Q1, Q2, Q3] = [0, 0, 0]

numeros = list(map(int, input().split())) # Recebe os números
numeros.sort() # Ordeena os números em ordem crescente

metade = int(N/2) # Identifica o meio da lista de números
quarto = int(metade/2) # Identifica onde está 1/4 da lista de números

if N%2 == 0: # Caso a quantidade de números seja par
  Q2 = (numeros[metade-1] + numeros[metade])/2 # Q2 é a média entre os dois números do centro

else:
  Q2 = numeros[metade] # Q2 recebe o valor do número no centro

if metade%2 == 0: # Caso o meio da lista seja par
  Q1 = (numeros[quarto-1] + numeros[quarto])/2 # Q1 é a média dos números que demarcam o fim do primeiro 1/4 da lista
  Q3 = (numeros[-(quarto+1)] + numeros[-quarto])/2 # Q# é a média dos números que demarcam o começo do quarto 1/4 da lista

else:
  Q1 = numeros[quarto] # Q1 é o número que demarca o fim primeiro 1/4 da lista
  Q3 = numeros[-(quarto+1)] # Q3 é o número que demarca o começo do quarto 1/4 da lista

print(Q1, Q2, Q3)