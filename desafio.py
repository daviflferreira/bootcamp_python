porcoes = float(input("Quantas porções por dia? "))
porcoes_produto = float(input("Quantas porções por produto? "))
dias = porcoes_produto / porcoes

print(f"O produto duraria {dias:.0f} dias. ")