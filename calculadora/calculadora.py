import calculadora.menu as menu
import operacoes


while True:
    menu.menu()# busca o modulo menu
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    operacao = input('Escolha a operação desejada !  ')
    operacoes.operacoes(num1, num2, operacao) # realiza o calculo
    
    sair = str(input('Deseja finalizar o calculo ? ')).upper()
    if sair == 'S':
        print('Saindo...')
        break
    novo = input('Deseja informar novos numeros? ').upper()
    if novo == 'S':
        continue
    hist = str(input('Deseja saber seu historico ? ')).upper()
    if hist == 'S':
        print(operacoes.historico) # busca dentro do modulo operacoes o historico
    