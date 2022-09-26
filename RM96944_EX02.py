#Os alunos da sua turma fizeram uma votação para escolher qual dia da semana
# é o melhor para a realização das lives. Desenvolva um programa em que o usuário
# informe a quantidade de votos que cada um dos
# 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira)
# obtiveram, verifique e exiba qual dia foi o escolhido.
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0
alunos = int(input("Quantos alunos irão votar?"))

for i in range(alunos):
    voto = int(input("Para o dia da semana da Live vote: \n1- SEGUNDA \n2 - TERÇA \n3 - QUARTA \n4 - QUINTA \n5 - SEXTA: \n"))
    if voto == 1:
        segunda = segunda + 1
    elif voto == 2:
        terca = terca + 1
    elif voto == 3:
        quarta = quarta + 1
    elif voto == 4:
        quinta = quinta + 1
    elif voto == 5:
        sexta = sexta + 1
    else: print("Voto inválido")

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print(f'\nO dia vencedor foi Segunda-feira com {segunda} votos')
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print(f'\nO dia vencedor foi Terça-feira com {terca} votos')
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print(f'\nO dia vencedor foi Quarta-feira com {quarta} votos')
elif quinta > segunda and quinta > quarta and quinta > terca and quinta > sexta:
    print(f'\nO dia vencedor foi Quinta-feira com {quinta} votos')
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print(f'\nO dia vencedor foi Sexta-feira com {sexta} votos')