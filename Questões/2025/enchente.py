N, L = map(int, input().split()) # Captura o número de bairros (N) e o limite da água (L)
bairros = dict()  # Cria um dicionário que armazena os bairros cadastrados

for _ in range(N): # Loop para capturar os bairros e o limite de água registrado
  B, A = map(int, input().split())

  if A > L: # Caso a água registrada ultrapasse o limite
    if bairros.get(B, 0) <= A: # No caso do bairro não ter sido registrado ainda ou o novo registro de água for maior que o anterior
        bairros[B] = A # Registra bairro e seu nivel de água
  
if len(bairros) > 0: #Caso tenha bairros que ultrapassam o limite
  for bairro in bairros: #Imprime os bairros
    print(bairro, bairros[bairro]) 

else: # Caso não tenha bairros que ultrapassem o limite
  print("nenhum") # Imprime Nenhum

# O que permitiu não nos preocuparmos com a chance de haverem bairros duplicados foi o uso do dicionário
# pois ele não permite que chaves duplicadas sejam inseridas, poupando nosso trabalho.  