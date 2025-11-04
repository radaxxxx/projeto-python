alunos = {}
nomes = set()

while True: 
    print("""
====MENU PRINCIPAL====
1- Cadastrar aluno 
2- Registrar aluno
3- Listar alunos e medias 
4- Buscar aluno 
5- Mostrar aprovados e reprovados 
6- Relatório 
0- Sair          
=======================
""")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        matricula = input("Matricula: ")
        nome = input("Nome: ")
        if nome in nomes:
            print("!ALUNO já cadastrado!")
        else:
            alunos[matricula] = (nome , ())
            nomes.add(nome) 
            print("ALUNO cadastrado com sucesso")
    elif opcao == "2":
        matricula =  input("Matricula do aluno: ")
        if matricula in alunos:
            nome, _= alunos[matricula]
            notas_temp = []
            for i in range (3):
                nota = float(input(f"Nota {i+1}: "))
                notas_temp.append(nota)
            alunos[matricula] = (nome, tuple(notas_temp))
            print("||Notas Registradas||")
        else:
            print("||NOtas não Registradas||")
    elif opcao == "3":
        for matricula, (nome, notas) in alunos.items():
            if notas: 
                media = sum(notas) / len(notas)
                print(f"{matricula} - {nome} : {notas} Média = {media:.2f}")
            else:
                print(f"{matricula} - {nome}: sem notas.")
        print()
    elif opcao == "4":
        nome_busca = input("Digite o nome do aluno: ").lower()
        achou = False 
        for  matricula, (nome, notas) in alunos.items():
            if nome. lower() == nome_busca:
                achou = True
                print(f"{matricula} - {nome}: {notas}")
        if not achou:
            print("||ALUNO não encontrado||")
    elif opcao == "5":
        for matricula, (nome, notas) in alunos.items():
            if notas:
                media = sum(notas) / len(notas)
                if media >= 7:
                    print(f"{nome} - aprovado ({media:.2f})")
                else:
                    print(f"{nome} - reprovado ({media:.2f})")
        print()
    elif opcao == "6":
        print("""
--- RELATÓRIOS ---
1 - Alunos cadastrados
2 - Médias individuais
3 - Aprovados e Reprovados
""")
        tipo = input("Escolha: ")
        if tipo == "1":
            for matricula, (nome, _) in alunos.items():
                print(f"{matricula} - {nome}")
        elif tipo == "2":
            for matricula, (nome, notas) in alunos.items():
                if notas:
                    media = sum(notas) / len(notas)
                    print(f"{nome} - Média: {media:.2f} ")
        elif tipo == "3":
            for matricula, (nome, notas) in alunos.items():
                if notas:
                    media = sum(notas) / len (notas)
                    situacao = "Aprovado" if media >= 7 else "Reprovado" 
                    print(f"{nome} - {situacao} ({media:2.f})")
            print()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção Inválida!")
