from random import randrange
print('Ola, seja bem vindo ao banco. Vamos realizar o seu cadastro!! \n\n\n')



def cadastro():
    global nome
    global agencia
    global conta

    nome = input('Por favor, digite o seu nome: ')
    agencia = randrange(2000, 9999)
    conta = randrange(10000, 99999)

    return print(f'Ola {nome}, seja bem vindo!!\nDados da sua conta:\nAgência: {agencia}\nConta: {conta}\n\n')

cadastro()

saldo = 0
limite_saque = 0
extrato = []

def deposito():
            global saldo
            global extrato

            verificador_agencia = int(input('Digite o numero do AGENCIA para deposito: '))
            verificador_conta = int(input('Digite o numero do CONTA para deposito: '))

            if verificador_agencia == agencia and verificador_conta == conta:
                valor_deposito = float(input('Por gentileza, digite o valor para realizar o depósito: '))
                if valor_deposito < 0:
                    print('Valor depósito inválido, tente novamente!')
                else:
                    saldo += valor_deposito
                    extrato.append(f'Deposito: R${valor_deposito:.2f}')
                    print('Deposito realizado com sucesso!')

def sacar(valor_saque):
        global limite_saque
        global extrato

        limite_saque += 1
        if limite_saque > 3:
            print('Limite de saque atingido, volte novamente amanhã!')
        else:
             
             if valor_saque > 500:
                 print('Valor de saque acima do limite. O seu limite é de R$500,00!')
             elif saldo > valor_saque:
                saldo -= valor_saque
                print(f'Saque no valor de R${valor_saque:.2f} realizado com sucesso!')
                print(limite_saque)
                extrato.append(f'Saque realizado: R${valor_saque:.2f}')  
             elif saldo < valor_saque:
                 print('Saldo insuficiente para saque!')

def exibir_extrato():
        global saldo
        global extrato

        print('EXTRATO'.center(20, '#'))
        print(f'saldo: R${saldo:.2f}')
        sep = '\n'
        print(f'{sep.join(extrato)} \n\n', end=' ')

while True:

    
    operacao = int(input('Por gentileza digite o numero que corresponde a operação desejada\n1 - Depositar\n2 - Sacar\n3 - visualizar o extrato\n4 - Sair\nOperação: '))

    #LOGICA DEPOSITO
    if operacao == 1:
        deposito()
    elif operacao == 2:
        sacar()
    elif operacao == 3:
        exibir_extrato()
    elif operacao == 4:
        break

