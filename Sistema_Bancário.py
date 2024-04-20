menu = """
===== Escolha uma das opções =====

[D] Depósitar
[S] Sacar
[E] Extrato
[Q] Sair

==>"""

saldo = 0
limite_adicional = 500
numeros_saques = 0
LIMITE_SAQUES = 3
extrato = ""

while True:
    opcao = input(menu).upper()
    
    if opcao == 'D':
        valor = float(input("Digite um valor para ser depositado: \n"))
        if valor > saldo:
            saldo += valor
            extrato += f"Depósito de: {valor:.2f}\n"
        else:
            print("Opcão inválida, por favor digite novamente")
    
    elif opcao == 'S':
        valor = float(input("Digite um valor para ser sacado: \n"))
        
        if numeros_saques >= LIMITE_SAQUES:
            print("Limite máximo de saques atingidos, tente novamente amanhã.")
            
        elif saldo < limite_adicional:
            limite_adicional -= valor
            extrato += f"Saque com limite adicional: R${valor:.2f}\n"
            numeros_saques += 1
            
        elif saldo >= valor:
            saldo -= valor
            extrato += f"Saque de: R${valor:.2f}\n"
            numeros_saques += 1
            
        else:
            print("Operação inválida, tente novamente.")
    
    elif opcao == 'E':
        print("======= Extrato bancário =======")
        print("Nao houveram movimentações" if not extrato else extrato)
        print(f"\nSaldo total: R${saldo:.2f}\nLimite adicional: R${limite_adicional:.2f}")
        print("\n===============================")
        
    elif opcao == 'Q':
        break
    
    else:
        print("Operação inválida, digite novamente.")
        
        
            
        
        
            
            
