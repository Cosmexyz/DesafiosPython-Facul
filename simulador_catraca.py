estado = 'TRAVADO'

while True: 

    açao = input('insira a passagem:\n')

    if estado == 'TRAVADO' and açao == 'moeda':
      estado = 'LIBERADO'
      print(estado)
      
    elif estado == 'LIBERADO' and  açao == 'empurrar':
       estado = 'TRAVADO'
       print(estado)
     
    if estado == 'TRAVADO':
      açao != 'moeda' and açao != 'empurrar'
      print('Insira a MOEDA, para liberar a passagem')

    