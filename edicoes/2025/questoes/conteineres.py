[a, b, c] = list(map(int, input().split())) # Recebe as dimensões dos conteineres
[x, y, z] = list(map(int, input().split())) # Recebe as dimensões do navio
print(int(x/a) * int(y/b) * int(z/c)) # Calcula a quantidade de conteineres que cabem no navio