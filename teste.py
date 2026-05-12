lista = []

while True:
    num = int(input("Digite números inteiros ou 0 para sair: "))


    if num == 0:
        break

    lista.append(num)


if len(lista) > 0:
    maior = max(lista)
    menor = min(lista)


    print("Quantidade de elementos na lista: ", end="")
    print(len(lista))
    print(f"Número maior: {maior}, número menor: {menor}")

else:
    print("A Lista está vazia.")