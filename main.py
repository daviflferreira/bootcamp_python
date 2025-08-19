from funcoes import saudacao, soma, verificar_maioridae


saudacao("Davi")
print(soma(2, 10))
minha_idade = int(input("Digite a sua idade: "))

if verificar_maioridae(minha_idade):
    print("Você é maior de idade")
else:
    print("Você é menor de idade")