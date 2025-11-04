CATEGORIAS = ("Alimentos", "Limpeza", "Bebidas")
produtos = []
codigos_cadastrados = set()

def cadastrar_produto():
    try:
        codigo = int(input("Código: ").strip())
    except ValueError:
        print("Código inválido. Use um número inteiro.")
        return
    if codigo in codigos_cadastrados:
        print("Código já existe.")
        return
    nome = input("Nome: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    try:
        preco = float(input("Preço: ").strip())
    except ValueError:
        print("Preço inválido.")
        return
    try:
        quantidade = int(input("Quantidade: ").strip())
    except ValueError:
        print("Quantidade inválida.")
        return

    for i, c in enumerate(CATEGORIAS, 1):
        print(f"{i} - {c}")
    try:
        idx = int(input("Categoria: ").strip())
        if idx < 1 or idx > len(CATEGORIAS):
            print("Categoria inválida.")
            return
        categoria = CATEGORIAS[idx - 1]
    except ValueError:
        print("Entrada inválida para categoria.")
        return

    produto = {"codigo": codigo, "nome": nome, "preco": preco, "quantidade": quantidade, "categoria": categoria}
    produtos.append(produto)
    codigos_cadastrados.add(codigo)
    print("Produto cadastrado.")

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for p in produtos:
        print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['quantidade']} | Categoria: {p['categoria']}")

def buscar_produto():
    try:
        codigo = int(input("Código: ").strip())
    except ValueError:
        print("Código inválido.")
        return
    for p in produtos:
        if p["codigo"] == codigo:
            print(f"Código: {p['codigo']} | Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Qtd: {p['quantidade']} | Categoria: {p['categoria']}")
            return
    print("Produto não encontrado.")

def atualizar_produto():
    try:
        codigo = int(input("Código: ").strip())
    except ValueError:
        print("Código inválido.")
        return
    for p in produtos:
        if p["codigo"] == codigo:
            nome = input("Novo nome (enter para manter): ").strip() or p["nome"]
            preco_in = input("Novo preço (enter para manter): ").strip()
            if preco_in:
                try:
                    preco = float(preco_in)
                except ValueError:
                    print("Preço inválido.")
                    return
            else:
                preco = p["preco"]
            quantidade_in = input("Nova quantidade (enter para manter): ").strip()
            if quantidade_in:
                try:
                    quantidade = int(quantidade_in)
                except ValueError:
                    print("Quantidade inválida.")
                    return
            else:
                quantidade = p["quantidade"]
            p.update({"nome": nome, "preco": preco, "quantidade": quantidade})
            print("Produto atualizado.")
            return
    print("Produto não encontrado.")

def excluir_produto():
    try:
        codigo = int(input("Código: ").strip())
    except ValueError:
        print("Código inválido.")
        return
    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            codigos_cadastrados.discard(codigo)
            print("Produto excluído.")
            return
    print("Produto não encontrado.")

def menu():
    try:
        while True:
            print("\n1-Cadastrar\n2-Listar\n3-Buscar\n4-Atualizar\n5-Excluir\n0-Sair")
            op = input("Opção: ").strip()
            if op == "1": cadastrar_produto()
            elif op == "2": listar_produtos()
            elif op == "3": buscar_produto()
            elif op == "4": atualizar_produto()
            elif op == "5": excluir_produto()
            elif op == "0": break
            else: print("Opção inválida.")
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo...")

if __name__ == "__main__":
    menu()