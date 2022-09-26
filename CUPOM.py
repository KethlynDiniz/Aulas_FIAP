valor_compra = input("Informe o valor da compra realizada: ")
cupom = input("Digite o código do cupom: ")

if cupom.upper() == "NIVER10":
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)

print("Cupom Inválido")

print(f' O valor final é {valor_final}')