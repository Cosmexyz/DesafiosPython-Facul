estado_luz = 'DESLIGADA'
estado_ar = 'DESLIGADO'
estado_janela = 'FECHADA'

while True:
    
    print('_' * 30)
    comando = input('Qual Comando: \nLigar Luz ou Desligar \nLigar ar ou Desligar \nAbrir janela ou fechar \nSair \n')

    # <<<< CICLO LUZ >>>>
    #LIGAR luz e confirmar status atual
    if estado_luz == 'DESLIGADA' and comando == 'ligar luz':
        estado_luz = 'LIGADA'
        print('Luz {}'.format(estado_luz))
    elif estado_luz == 'DESLIGADA' and comando == 'desligar luz':
        print('A luz já está {}'.format(estado_luz))

    #DESLIGAR luz e confirmar status atual
    elif estado_luz == 'LIGADA' and comando == 'desligar luz':
        estado_luz = 'DESLIGADA'
        print('Luz {}'.format(estado_luz))
    elif estado_luz == 'LIGADA' and comando == 'ligar luz':
        print('A luz já está {}'.format(estado_luz))

    # <<<< CICLO AR >>>>
    # interasão entre janela e ar
    elif estado_janela == 'ABERTA' and comando == 'ligar ar':
        print('O Ar-condicionado não pode ser ligado enquanto a janela está aberta, feche a janela')
    #LIGAR ar e confirmar status atual
    elif estado_ar == 'DESLIGADO' and comando == 'ligar ar':
        estado_ar = 'LIGADO'
        print('Ar {}'.format(estado_ar))
    elif estado_ar == 'DESLIGADO' and comando == 'desligar ar':
        print('O ar já está {}'.format(estado_ar))

    #DESLIGAR ar e confirmar status atual
    elif estado_ar == 'LIGADO' and comando == 'desligar ar':
        estado_ar = 'DESLIGADO'
        print('Ar {}'.format(estado_ar))
    elif estado_ar == 'LIGADO' and comando == 'ligar ar':
        print('O ar já está {}'.format(estado_ar))

   # <<<< CICLO JANELA >>>>
   #FECHAR janela e confirmar status atual
    elif estado_janela == 'FECHADA' and comando == 'abrir janela':
        estado_janela = 'ABERTA'
        print('Janela {}'.format(estado_janela))
    elif estado_janela == 'FECHADA' and comando == 'fechar janela':
        print('A janela já está {}'.format(estado_janela))

    #ABRIR janela e confirmar status atual
    elif estado_janela == 'ABERTA' and comando == 'fechar janela':
        estado_janela = 'FECHADA'
        print('Janela {}'.format(estado_janela))
    elif estado_janela == 'ABERTA' and comando == 'abrir janela':
        print('A janela já está {}'.format(estado_janela))
    
    # <<<< SAIR DO CICLO >>>>
    elif comando == 'sair':
        print('Saindo....')
        break
    else:
        print('Comando Inválido')