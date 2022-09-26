# Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver
# um trabalho em parceria:
# um serviço em que as pessoas possam usar um estúdio profissional para gravar seus
# vídeos para o YouTube com máxima qualidade.
# O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por
# uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

fat_anual = float(input("Insira seu faturalmento anual em reais: "))
plano = input("Insira o plano escolhido: Basic, Silver, Gold, Platinum: ")

if plano.upper() == "BASIC":
    bonus = fat_anual * 0.3
    print(f'O valor do bônus a ser pago será de R${bonus}')
elif plano.upper() == "SILVER":
    bonus = fat_anual * 0.2
    print(f'O valor do bônus a ser pago será de R${bonus}')
elif plano.upper() == "GOLD":
    bonus = fat_anual * 0.1
    print(f'O valor do bônus a ser pago será de R${bonus}')
elif plano.upper() == "PLATINUM":
    bonus = fat_anual * 0.05
    print(f'O valor do bônus a ser pago será de R${bonus}')
else:
    print("O plano escolhido não existe, tente novamente.")