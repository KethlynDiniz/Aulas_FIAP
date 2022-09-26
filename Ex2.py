valor_pacote = float(input("Digite o valor do pacote: "))
categoria = str(input("Digite em qual classe irá voar: "))
viajantes = float(input("Digite a quantidade de pessoas que irão viajar: "))

if categoria == "Econômica":
    if viajantes == 2:
        valor_final = valor_pacote * 0.03
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes == 3:
        valor_final = valor_pacote * 0.04
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes >= 4:
        valor_final = valor_pacote * 0.05
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    else:
        print(f'Viagem para uma pessoa não gera desconto. Valor total R$ {valor_pacote}')

if categoria == "Executiva":
    if viajantes == 2:
        valor_final = valor_pacote * 0.05
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes == 3:
        valor_final = valor_pacote * 0.07
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes >= 4:
        valor_final = valor_pacote * 0.08
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    else:
        print(f'Viagem para uma pessoa não gera desconto. Valor total R$ {valor_pacote}')

if categoria == "Primeira Classe":
    if viajantes == 2:
        valor_final = valor_pacote * 0.1
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes == 3:
        valor_final = valor_pacote * 0.15
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    elif viajantes >= 4:
        valor_final = valor_pacote * 0.2
        print(f'Valor do pacote R${valor_pacote}')
        print(f'Valor com desconto: R${valor_pacote - valor_final}')
        print(f'Valor médio por pessoa: R${(valor_pacote - valor_final) / viajantes}')
    else:
        print(f'Viagem para uma pessoa não gera desconto. Valor total R$ {valor_pacote}')