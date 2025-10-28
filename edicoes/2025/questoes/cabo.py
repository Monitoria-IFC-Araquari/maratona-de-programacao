[A, B] = map(int, input().split()) # Recebe a quantidade de pessoas nos times A e B

N = A+B

L_A = [] # Cria uma lista para as forças das pessoas do time A
L_B = [] # Cria uma lista para as forças das pessoas do time B

# Nesta linha foi utilizado list comprehension, ela equivale ao código comentado abaixo
[L_A.append(int(_[1])) if _[0] == "A" else L_B.append(int(_[1])) for _ in input().split()] 


#for _ in input().split(): # Percorre as pessoas inseridas
#    if _[0] == "A": # Caso a pessoa seja do time A a sua força é adicionada para a lista do time A
#        L_A.append(int(_[1]))
#
#    else: # Caso não a sua força é adicionada na lista do time B
#        L_B.append(int(_[1]))



M_A = sum(L_A)/A # Calcula a força média do time A
M_B = sum(L_B)/B # Calcula a força média do time B


# Realiza as comparações e imprime o resultado
if M_A < M_B:
    print("B")
    
elif M_A > M_B:
    print("A")

else: 
    print("E")