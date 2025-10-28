N = int(input()) # Recebe o número de letras em que o alfabeto será movido
T = int(input()) # Recebe o tamanho da palavra que será criptografada

alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split() # Cria uma lista com o alfabeto
novo_alfabeto = alfabeto.copy() # Cria uma cópia da lista com o alfabeto
P = input().upper() # Recebe a palavra que será criptografada e deixa todas as suas letras em caixa alta

for i in range(N): # Altera o "novo_alfabeto" para que ele seja correspondente a criptografia
    letra_trocada = novo_alfabeto.pop(0) # Remove a primeira letra do alfabeto e armazena ela em uma variável
    novo_alfabeto.append(letra_trocada) # Adiciona a letra armazenada no final do alfabeto

txt = "" 
for i in range(T): # Forma a nova palavra
    txt += novo_alfabeto[alfabeto.index(P[i])] # Encontra o índice da letra no alfabeto original e então, procura a letra equivalente no novo alfabeto

print(txt)