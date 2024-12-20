nome = input('Seja bem vindo, digite o seu nome: ')
print(f'Ola {nome} seja bem vindo ao nosso banco \n\n')
saldo = 0
limite_saque = 0
extrato = []

while True:
    operacao = int(input('Por gentileza digite o numero que corresponde a operação desejada\n1 - Depositar\n2 - Sacar\n3 - visualizar o extrato\n4 - Sair\nOperação: '))

    if operacao == 1:
        valor_deposito = float(input('Por gentileza, digite o valor para realizar o depósito: '))
        if valor_deposito < 0:
            print('Valor depósito inválido, tente novamente!')
        else:
            saldo += valor_deposito
            extrato.append(f'Deposito: R${valor_deposito}')
            print('Deposito realizado com sucesso!')
    elif operacao == 3:
        print(f'saldo: {saldo}')
        sep = '\n'
        print(f'{sep.join(extrato)} \n', end=' ')
    elif operacao == 4:
        break

