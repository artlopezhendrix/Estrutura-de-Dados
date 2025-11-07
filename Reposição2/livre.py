# A pilha de livros será representada por uma lista
pilha_de_livros = []

def empilhar_livro(titulo):
    """Adiciona um livro (push) ao topo da pilha."""
    pilha_de_livros.append(titulo)
    print(f"\n✅ Livro '{titulo}' empilhado com sucesso!")

def desempilhar_livro():
    """Remove e pega o livro do topo da pilha (pop)."""
    if pilha_de_livros:
        livro_pego = pilha_de_livros.pop()
        print(f"\n❌ Você pegou o livro: '{livro_pego}'.")
    else:
        print("\n⚠️ A pilha de livros está vazia.")

def ver_topo():
    """Mostra o livro no topo da pilha sem pegá-lo (peek)."""
    if pilha_de_livros:
        livro_topo = pilha_de_livros[-1]
        print(f"\n🔝 O livro no topo da pilha é: '{livro_topo}'.")
    else:
        print("\n⚠️ A pilha de livros está vazia.")

def mostrar_pilha():
    """Exibe todos os livros da base (primeiro empilhado) até o topo (último empilhado)."""
    if not pilha_de_livros:
        print("\n⚠️ A pilha está vazia.")
        return

    print("\n📖 Livros na Pilha (Base -> Topo):")
    # Itera para mostrar a ordem
    for i, livro in enumerate(pilha_de_livros):
        if i == len(pilha_de_livros) - 1:
            print(f"   [TOPO] -> {livro} (Próximo a ser pego)")
        else:
            print(f"          -> {livro}")
    print("-" * 30)


def menu_livros():
    """Menu interativo para a simulação da pilha de livros."""
    while True:
        print("\n" + "=" * 30)
        print("📚 Pilha de Livros na Mesa (LIFO)")
        print("=" * 30)
        print("1 - Empilhar um novo livro")
        print("2 - Pegar (Desempilhar) o livro do topo")
        print("3 - Ver qual livro está no topo")
        print("4 - Visualizar a pilha completa")
        print("5 - Sair")
        print("-" * 30)

        try:
            opcao = input("Digite sua escolha: ")
            
            if opcao == '1':
                titulo = input("Informe o título do livro para empilhar: ")
                empilhar_livro(titulo)
            
            elif opcao == '2':
                desempilhar_livro()
            
            elif opcao == '3':
                ver_topo()
            
            elif opcao == '4':
                mostrar_pilha()
            
            elif opcao == '5':
                print("\n👋 Saindo da simulação da Pilha de Livros.")
                break
            
            else:
                print("\n❌ Opção inválida. Escolha um número de 1 a 5.")

        except ValueError:
            print("\n❌ Entrada inválida. Por favor, insira um número.")

# Executa o menu principal
if __name__ == "__main__":
    menu_livros()