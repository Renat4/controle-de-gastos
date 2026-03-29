gastos = []

while True:
    print("\n1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        
        gastos.append((descricao, valor))
        print("Gasto adicionado!")

    elif opcao == "2":
        for gasto in gastos:
            print(gasto)

    elif opcao == "3":
        break