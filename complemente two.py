opc = int(input('====== BEM VINDO AO MENU ======\nQUAL FUNCIONALIDADE VOCÊ DESEJA ?\n[1]ÁGUA NECESSARIA POR DIA\n'
          '[2]TAXA METABOLICA BASAL\n[3]CALCULO MACRO'))
if opc == 1:
    print('========== ÁGUA NECESSARIA POR DIA ==========')
    agua = 0.035
    peso = int(input('INFORME SEU PESO'))
    temperatura = int(input('INFORME A TEMPERATURA'))
    agua = agua * peso
    agua = agua + 0.003 * temperatura
    status = int(input('GRAU DE EXERCICIO NO DIA\n [1] BAIXO \n [2] MODERADO\n [3] ALTO'))
    while status > 3:
        status = int(input('NUMERO INVALIDO.\n [1] BAIXO \n [2] MODERADO\n [3] ALTO '))
    if status == 2:
        agua = (agua + 0.5)
        print('A QUANTIDADE DE AGUA NECESSARIA É {}'.format(agua))
    elif status == 3:
        agua = agua + 1
        print('A QUANTIDADE DE AGUA NECESSARIA É {}'.format(agua))
    elif status == 1:
        agua = agua + 0.2
        print('A QUANTIDADE DE AGUA NECESSARIA É {}'.format(agua))
    else:
        print('A QUANTIDADE DE AGUA NECESSARIA É {}'.format(agua))
        quit()
if opc == 2:
    alt = int(input('INFORME SUA ALTURA'))
    peso = int(input('INFORME SEU PESO'))
    idade = int(input('INFORME SUA IDADE'))
    TBM = (10 * peso) + (6.25 * alt) - (5 * idade) + 5
    ativ = int(input('[1] SEDENTADIO\n[2] LEVEMENTO ATIVO\n[3] MODERADAMENTE ATIVO\n[4] MUITO ATIVO\n[5] SUPER ATIVO'))
    if ativ == 1:
        TBM = TBM * 1.2
    elif ativ == 2:
        TBM = TBM * 1.375
    elif ativ == 3:
        TBM = TBM * 1.5
    elif ativ == 4:
        TBM = TBM * 1.734
    elif ativ == 5:
        TBM = TBM * 1.9
    ref = int(input('REFEIÇÕES AO DIA'))
    kcalref = TBM / ref
    carb = ((40 * TBM / 100) / ref) / 4
    prot = ((30 * TBM / 100) / ref) / 4
    gord = ((30 * TBM / 100) / ref) / 9
    print(f' Kcal por dia {TBM}\n Kcal por refeição {kcalref}\n Carboidrato por refeição {carb}\n '
          f'proteina por refeição'f' {prot}\n 'f'gordura por refeição {gord}')
    quit()
if opc == 3:
    proteina = 0
    gordura = 0
    carboidrato = 0
    prot = []
    gord = []
    carb = []
    kcal = []
    opcao = int(input('Sera consumido alguma carne ? [1] SIM [2] não'))
    if opcao != 2:
        itens = int(input('=== INFORME A QUANTIDADE DE ITENS ==='))
        for i in range(0, itens):
            carda = int(input('[1]MAMINHA\n[2]TILÁPIA\n[3]FRANGO\n[4]COXA DE FRANGO\n[5]LOMBO DE PORCO\n'
                              '[6]PATINHO\n[7]SALMÃO'))
            if carda == 1:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.2829 * gramas
                gordura = 0.0533 * gramas
                kcall = proteina * 4
                kcall = kcall + gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 2:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.3 * gramas
                gordura = 0.11 * gramas
                kcall = proteina * 4
                kcall = kcall + gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 3:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.3102 * gramas
                gordura = 0.0357 * gramas
                kcall = proteina * 4
                kcall = kcall + gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 4:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.268 * gramas
                gordura = 0.116 * gramas
                kcall = proteina * 4
                kcall = kcall + gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 5:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.2143 * gramas
                gordura = 0.0566 * gramas
                kcall = proteina * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 6:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.33 * gramas
                gordura = 0.0636 * gramas
                kcall = proteina * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
            elif carda == 7:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.2397 * gramas
                godura = 0.0756 * gramas
                kcall = proteina * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                kcal.append(kcall)
    opcao = int(input('SERA CONSUMIDO ALGUMA FRUTA ? [1] SIM [2] NÃO'))
    if opcao != 2:
        itens = int(input('=== INFORME A QUANTIDADE DE ITENS ==='))
        for h in range(0, itens):
            carda = int(input('[1]LIMÃO\n[2]KIWI\n[3]BANANA\n[4]ACABACATE\n[5]PERA'))
            if carda == 1:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.011 * gramas
                gordura = 0.003 * gramas
                carboidrato = 0.0932 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 2:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0114 * gramas
                gordura = 0.0052 * gramas
                carboidrato = 0.1466 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 3:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0109 * gramas
                gordura = 0.0033 * gramas
                carboidrato = 0.2284 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 4:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.02 * gramas
                gordura = 0.1466 * gramas
                carboidrato = 0.0853 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 5:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0038 * gramas
                gordura = 0.0012 * gramas
                carboidrato = + 0.1546 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
    opcao = int(input('SERA CONSUMIDO ALGUMA VERDURA ? [1] SIM [2] NÃO'))
    if opcao != 2:
        itens = int(input('=== INFORME A QUANTIDADE DE ITENS ==='))
        for v in range(0, itens):
            carda = int(input('[1]CENOURA\n[2]ALHO\n[3]CEBOLA\n[4]ALFACE\n[5]PEPINO'))
            if carda == 1:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0093 * gramas
                gordura = 0.0024 * gramas
                carboidrato = 0.958 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 2:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.636 * gramas
                gordura = 0.005 * gramas
                carboidrato = 0.3306 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 3:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0092 * gramas
                gordura = 0.0008 * gramas
                carboidrato = 0.1011 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 4:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.009 * gramas
                gordura = 0.0014 * gramas
                carboidrato = 0.0297 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 5:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0065 * gramas
                gordura = 0.0011 * gramas
                carboidrato = 0.0363 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
    opcao = int(input('SERA CONSUMIDO GRAOS ?[1] SIM [2] NÃO'))
    if opcao != 2:
        itens = int(input('=== INFORME A QUANTIDADE DE ITENS ==='))
        for g in range(0, itens):
            carda = int(input('[1]ARROZ\n[2]FEIJÃO\n[3]LINHAÇA\n[4]ERVILHA\n[5]TAPIOCA\n[6]AMENDOIM'))
            if carda == 1:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.025 * gramas
                gordura = 0.0023 * gramas
                carboidrato = 0.2818 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 2:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0867 * gramas
                gordura = 0.005 * gramas
                carboidrato = 0.228 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 3:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.17982 * gramas
                gordura = 0.3996 * gramas
                carboidrato = 0.01332 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 4:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.0542 * gramas
                gordura = 0.0004 * gramas
                carboidrato = 0.1446 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 5:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0 * gramas
                gordura = 0 * gramas
                carboidrato = 0.12 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
            elif carda == 6:
                gramas = int(input('INFORME OS GRAMAS'))
                proteina = 0.258 * gramas
                gordura = 0.4924 * gramas
                carboidrato = 0.1613 * gramas
                kcall = (proteina + carboidrato) * 4
                kcall += gordura * 9
                prot.append(proteina)
                gord.append(gordura)
                carb.append(carboidrato)
                kcal.append(kcall)
    for p in prot, kcal, carb, gord:
        proteina = sum(prot)
        gordura = sum(gord)
        carboidrato = sum(carb)
    print('A QUANTIDADE DE PROTEINA NESSA REFEIÇÃO É {}\nA QUANTIDADE DE GORDURA NESSA REFEIÇÃO É {}\n'
          'A QUANTIDADE DE CARBOIDRATO NESSA REFEIÇÃO É {}'.format(proteina, gordura, carboidrato))
