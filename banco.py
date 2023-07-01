
menu = '''
|==============================|
|           Opções             |
| [ d ] = Deposito             |
|                              |
| [ s ] = Saque                |
|                              |
| [ e ] = Extrato              |
|                              |
| [ x ] = Sair                 |
|==============================|
'''
saldo = 0

limite_saque_diario = 3
contador = 0

extrato = []

while True:
    
    print(menu)
    escolha = input(f'Escolha uma opção: ')
    escolha = escolha.lower()

    if escolha == 'd':
        deposito = float(input('Digite o valor que deseja ser depositado: '))
        deposito = round(deposito,2)
        if deposito >= 0:
            saldo += deposito
            adicionar_deposito = f'R$ {deposito}'
            adicionar_extrato_deposito = f'Deposito R$ {deposito}'
            extrato.append(adicionar_extrato_deposito)
            print(f'Deposito feito no valor de R$ {adicionar_deposito}')
            
        else:
            print('Valor invalido digite um valor positivo')

    elif escolha == 's':
        saque = float(input('Digite o valor que deseja ser sacar: '))
        if saque > saldo:
            print(f'Saldo insuficiente, seu saldo atual é de {saldo}')

        elif contador < limite_saque_diario and saque <= 500:
            saldo -= saque
            adicionar_saque = f'R$: - {saque}'
            adicionar_extrato_saque = f'Saque R$ - {saque}'
            extrato.append(adicionar_extrato_saque)
            print(f'Saque feito no valor de R$ {adicionar_saque}')
            contador += 1

        elif saque > 500:
            print('Você esta tentando sacar a cima do limite permitido, que é de R$ 500')

        elif contador == limite_saque_diario:
            print('Limite de saque diario atingido')        

    elif escolha == 'e':
        indice = 0
        if len(extrato) == 0:
            print('===== EXTRATO ======================')
            print('Não foram realizadas movimentações.')
            print('====================================')
        else:        
            print('===== EXTRATO =====')
            while indice < len(extrato):
                print(extrato[indice])
                indice += 1
            print(f'Saldo: R$ {saldo}')
            print('===================')

    elif escolha == 'x':
        break

    else:
        print('Opção invalida, porfavor seleciona uma opção valida')

