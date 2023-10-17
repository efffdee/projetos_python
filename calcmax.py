#CALCULADORA COM OPERAÇÕES SIMPLES (+-*/) UTILIZANDO IF E WHILE.


print('====================================')
print('====================================')
print('-------------CALC MAX---------------')
print('====================================')
print('====================================')

resultado = 0

operacao = input('Deseja realizar uma operação matemática? [S] ou [N] ').upper()


while operacao == 'S':

        primeiro_numero = float(input('Digite o primeiro número: '))
        operador = input('ESCOLHA: [+] SOMAR | [-] SUBTRAIR | [*] MULTIPLICAR [/] DIVIDIR ')
        segundo_numero  = float(input('Digite o segundo número: '))

        if operador == "+":
            resultado = primeiro_numero + segundo_numero
            print(f'O resultado é = {resultado}')

        elif operador == "-":
            resultado = primeiro_numero - segundo_numero
            print(f'O resultado é = {resultado}')
        elif operador == "*":
            resultado = primeiro_numero * segundo_numero
            print(f'O resultado é = {resultado}')
        elif operador == "/":
            resultado = primeiro_numero / segundo_numero
            print(f'O resultado é = {resultado}')
    

        operacao = input('Deseja fazer outra operação? ([S] ou [N]): ').upper()

if operacao == 'N':
    print('OBRIGADO POR UTILIZAR A CALC MAX!')
    print('CONTE SEMPRE COM A GENTE!')    
    
elif operacao != 'S' or 'N':
    print('CHEGA DE ZOEIRA! ATÉ A PRÓXIMA!')