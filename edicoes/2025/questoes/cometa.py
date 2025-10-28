A = int(input()) # Recebe o ano atual

M = (A - 1986) % 76 # Calcula quantos anos se passaram dese a ultima vez em que o cometa passou
print(A + (76 - M)) # Calcula quantos anos faltam para o cometa passar novamente e soma isso ao ano atual, então imprime o resultado