historico = []

def operacoes(num1, num2, simbolo): #informa os valores e a operação
    calculo = f'{num1} {simbolo} {num2}' #mostra a operação para ser executada
    resultado = eval (calculo)
    print(eval(calculo)) #transforma o que eh string em operação

    historico.append(resultado) #add o resultado na lista historico
    