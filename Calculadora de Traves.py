print(" ---------- CALCULADORA DE TRAVES ---------- ")
print("\n")
valor_super = float(input("Digite o valor total em R$: "))
odd_super = float(input("Digite a odd da superbet: "))
odd_mais = float(input("Digite a odd do mais traves: "))
total = (valor_super * odd_super) / odd_mais
ganho_total = total * odd_mais
lucro = ganho_total - (valor_super + total)
print("\n")
print(f"Deve apostar no mais traves: {total:.2f}")
print(f"Retorno Total: {ganho_total:.2f}")
print(f"Lucro: {lucro:.2f}" )







