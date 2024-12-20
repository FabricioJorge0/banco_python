nome = input('Seja bem vindo, digite o seu nome: ')
print(f'Ola {nome} seja bem vindo ao nosso banco \n\n')
saldo = 0
limite_saque = 0
extrato = []

while True:

    
    operacao = int(input('Por gentileza digite o numero que corresponde a operação desejada\n1 - Depositar\n2 - Sacar\n3 - visualizar o extrato\n4 - Sair\nOperação: '))

    #LOGICA DEPOSITO
    if operacao == 1:
        valor_deposito = float(input('Por gentileza, digite o valor para realizar o depósito: '))
        if valor_deposito < 0:
            print('Valor depósito inválido, tente novamente!')
        else:
            saldo += valor_deposito
            extrato.append(f'Deposito: R${valor_deposito:.2f}')
            print('Deposito realizado com sucesso!')
    elif operacao == 2:
        limite_saque += 1
        if limite_saque > 3:
            print('Limite de saque atingido, volte novamente amanhã!')
        else:
             valor_saque = float(input('Por gentileza digite o valor para saque: '))
             if valor_saque > 500:
                 print('Valor de saque acima do limite. O seu limite é de R$500,00!')
             elif saldo > valor_saque:
                saldo -= valor_saque
                print(f'Saque no valor de R${valor_saque:.2f} realizado com sucesso!')
                print(limite_saque)
                extrato.append(f'Saque realizado: R${valor_saque:.2f}')  
             elif saldo < valor_saque:
                 print('Saldo insuficiente para saque!')
    elif operacao == 3:
        print('EXTRATO'.center(20, '#'))
        print(f'saldo: R${saldo:.2f}')
        sep = '\n'
        print(f'{sep.join(extrato)} \n\n', end=' ')
    elif operacao == 4:
        break

