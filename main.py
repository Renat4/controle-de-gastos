gastos = []

while True:
    print("\n1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        descricao = input("Descrição: ")
        valor = float(input("Valor: "))
        
        gastos.append({
            "descricao": descricao,
            "valor": valor
        })

    elif opcao == "2":
        if not gastos:
            print('Nenhum gasto registrado')
        else:
            print('=-' *10)
            for gasto in gastos:
                print(f"{gasto['descricao']} - R$ {gasto['valor']}")

            total = 0
            for gasto in gastos:
                total += gasto["valor"]
            print(f'Total gasto: R$ {total}')

    elif opcao == "3":
        print('Saindo...')
        break