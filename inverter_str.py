nome = str(input('Digite seu nome:\n')).strip().lower()
indice = len(nome)-1
inverter_nome = ''

while indice >= 0:
    inverter_nome = inverter_nome + nome[indice]
    indice -= 1
    
print('O nome digitado foi: {} \nQue ao contrario é: {}'.format(nome, inverter_nome))
