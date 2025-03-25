estudantes = ["Joao", "Maria", "Jose", "Carol"]
professores = ["Thiago", "Igor", "Marcos", "Raquel"]
disciplinas = ["Matemática", "Educação Física", "Filosofia", "História"]
turmas = ["01", "02", "03", "04"]
matriculas = ["001", "002", "003", "004"]

# Variáveis para controle do contexto atual
lista_atual = []
nome_categoria = ""

# Menu principal
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("(1) Gerenciar estudantes")
    print("(2) Gerenciar professores")
    print("(3) Gerenciar disciplinas")
    print("(4) Gerenciar turmas")
    print("(5) Gerenciar matrícula")
    print("(0) Sair\n")

    opcao = input("Digite uma opção válida: ")
    
    if opcao == "0":
        print("Saindo do sistema...")
    # Definindo a categoria de trabalho
    elif opcao == "1":
        lista_atual = estudantes
        nome_categoria = "estudantes"
    elif opcao == "2":
        lista_atual = professores
        nome_categoria = "professores"
    elif opcao == "3":
        lista_atual = disciplinas
        nome_categoria = "disciplinas"
    elif opcao == "4":
        lista_atual = turmas
        nome_categoria = "turmas"
    elif opcao == "5":
        lista_atual = matriculas
        nome_categoria = "matrículas"
    else:
        print("Opção inválida!")
        continue

    # Menu secundário
    while True:
        print(f"\n--- GERENCIANDO {nome_categoria.upper()} ---")
        print("(1) Listar")
        print("(2) Incluir")
        print("(3) Atualizar")
        print("(4) Excluir")
        print("(5) Voltar ao menu anterior")

        opcao_secundaria = input("Digite uma opção válida: ")

        if opcao_secundaria == "1":
            print(f"\nLista de {nome_categoria}:")
            for indice, item in enumerate(lista_atual, 1):
                print(f"{indice}. {item}")

        elif opcao_secundaria == "2":
            novo_item = input(f"\nDigite o novo {nome_categoria[:-1]}: ")
            lista_atual.append(novo_item)
            print("Adicionado com sucesso!")

        elif opcao_secundaria == "3":
            indice = int(input(f"\nDigite o número do item para atualizar (1-{len(lista_atual)}): ")) - 1
            if 0 <= indice < len(lista_atual):
                novo_valor = input("Digite o novo valor: ")
                lista_atual[indice] = novo_valor
                print("Atualizado com sucesso!")
            else:
                print("Índice inválido!")

        elif opcao_secundaria == "4":
            indice = int(input(f"\nDigite o número do item para excluir (1-{len(lista_atual)}): ")) - 1
            if 0 <= indice < len(lista_atual):
                removido = lista_atual.pop(indice)
                print(f"'{removido}' removido com sucesso!")
            else:
                print("Índice inválido!")

        elif opcao_secundaria == "5":
            break

        else:
            print("Opção inválida!")