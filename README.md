# projeto-python
Projeto 1- Joáo Manoel de Sousa.
📦 Sistema de Gerenciamento de Produtos
📋 Descrição
Sistema completo para controle de estoque de produtos com categorias pré-definidas.

🎯 Funcionalidades
Opção	Descrição
1. Cadastrar	Adiciona novo produto ao sistema
2. Listar	Exibe todos os produtos cadastrados
3. Buscar	Localiza produto por código
4. Atualizar	Edita informações do produto
5. Excluir	Remove produto do sistema
0. Sair	Encerra o programa
🏷️ Categorias Disponíveis
🍎 Alimentos
🧼 Limpeza
🥤 Bebidas
💡 Exemplo de Uso
python
# Cadastrando um produto
Opção: 1
Código: 1001
Nome: Arroz Integral
Preço: 8.50
Quantidade: 30
1 - Alimentos
2 - Limpeza
3 - Bebidas
Categoria: 1
✅ Produto cadastrado.
🛡️ Validações
✅ Código único para cada produto
✅ Nome não pode ser vazio
✅ Preço deve ser numérico
✅ Quantidade deve ser inteira
✅ Categoria deve existir

 Projeto 2 - Ryan Porto Antunes
 🎓 Sistema de Gerenciamento de Alunos
📚 Descrição
Sistema acadêmico para cadastro de alunos, registro de notas e geração de relatórios.
🎯 Menu Principal
text
MENU PRINCIPAL 
1- Cadastrar aluno
2- Registrar notas
3- Listar alunos e médias
4- Buscar aluno
5- Aprovados/Reprovados
6- Relatórios
0- Sair

📊 Funcionalidades Detalhadas
1. Cadastrar Aluno
Matrícula e nome do aluno
Verifica se nome já existe
2. Registrar Notas
3 notas por aluno
Cálculo automático da média
3. Listar Alunos
Exibe todos alunos com notas e médias
Formato: MAT001 - João: (7.5, 8.0, 6.5) Média = 7.33
4. Buscar Aluno
Busca por nome (não diferencia maiúsculas/minúsculas)
5. Aprovados/Reprovados
Média ≥ 7.0: Aprovado
Média < 7.0: Reprovado
6. Relatórios
text
--- RELATÓRIOS ---
1 - Alunos cadastrados
2 - Médias individuais
3 - Aprovados e Reprovados
💡 Exemplo de Uso
python
# Cadastrando aluno
Opção: 1
Matricula: 2024001
Nome: Maria Silva
✅ ALUNO cadastrado com sucesso
# Registrando notas
Opção: 2
Matricula do aluno: 2024001
Nota 1: 8.5
Nota 2: 7.0
Nota 3: 9.0
✅ ||Notas Registradas||
# Verificando situação
Opção: 5
Maria Silva - aprovado (8.17)
📈 Critério de Avaliação
Aprovado: Média ≥ 7.0
Reprovado: Média < 7.0

