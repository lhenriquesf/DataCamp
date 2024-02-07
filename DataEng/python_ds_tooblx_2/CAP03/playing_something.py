#%%
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

input_user = input('Number: ')
flag = True
while flag:
    if input_user.isdigit():
        flag = False
        input_user_int = int(input_user)
        par_ou_impar = f'{input_user_int} é Par' if input_user_int%2==0 else f'{input_user_int} é Impar'
        print(par_ou_impar)
    else:
        print(f'{input_user} não é um inteiro')
        input_user = input('Digite novamente o Number: ')
