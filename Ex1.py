
idade = int(input("Digite sua idade: "))
bpm = int(input("Digite seus batimentos por minuto (BPM): "))

if idade <= 8:
    if bpm < 120:
            print("Abaixo da faixa adequada")
    elif bpm >= 120 and bpm <= 140:
            print("Dentro da faixa adequada")
    elif bpm > 140:
            print("Acima da faixa adequada")

elif idade > 8 and idade <= 17:
    if bpm < 80:
            print("Abaixo da faixa adequada")
    elif bpm >= 80 and bpm <= 100:
            print("Dentro da faixa adequada")
    elif bpm > 100:
            print("Acima da faixa adequada")

elif idade > 17 and idade <= 60:
    if bpm < 70:
            print("Abaixo da faixa adequada")
    elif bpm >= 70 and bpm <= 80:
            print("Dentro da faixa adequada")
    elif bpm > 80:
            print("Acima da faixa adequada")

elif idade > 60:
    if bpm < 50:
            print("Abaixo da faixa adequada")
    elif bpm >= 50 and bpm <= 60:
            print("Dentro da faixa adequada")
    elif bpm > 60:
            print("Acima da faixa adequada")

else:
    print("Não foi possivel calcular")