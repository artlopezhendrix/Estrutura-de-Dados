# A pilha será representada por uma lista Python
sanduiche = []

def adicionar_ingrediente(ingrediente):
    """Adiciona um ingrediente (elemento) ao topo da pilha (sanduíche)."""
    sanduiche.append(ingrediente)
    print(f"\n✅ '{ingrediente}' foi adicionado ao sanduíche.")

def remover_ingrediente():
    """Remove e retorna o ingrediente do topo da pilha (o último adicionado)."""
    if sanduiche:
        ingrediente_removido = sanduiche.pop()
        print(f"\n❌ '{ingrediente_removido}' foi removido do topo do sanduíche.")
    else:
        print("\n⚠️ O sanduíche está vazio. Não há ingredientes para remover.")

def ver_ultimo_ingrediente():
    """Mostra o ingrediente no topo da pilha sem removê-lo (peek)."""
    if sanduiche:
        # Acessa o último elemento da lista
        ultimo_ingrediente = sanduiche[-1]
        print(f"\n🔝 O último ingrediente adicionado (topo da pilha) é: '{ultimo_ingrediente}'.")
    else:
        print("\n⚠️ O sanduíche está vazio.")

def mostrar_sanduiche():
    """Exibe todos os ingredientes, do pão de baixo (base) até o topo (último adicionado)."""
    if not sanduiche:
        print("\n⚠️ O sanduíche está vazio. Adicione alguns ingredientes!")
        return

    print("\n📜 Ingredientes do Sanduíche (do Pão de Baixo até o Topo):")
    # Para visualizar a ordem de empilhamento (base -> topo), iteramos a lista.
    for i, ingrediente in enumerate(sanduiche):
        # Adicionando indicadores visuais
        if i == 0:
            print(f"   [BASE] -> {ingrediente}")
        elif i == len(sanduiche) - 1:
            print(f"   [TOPO] -> {ingrediente} (Último adicionado)")
        else:
            print(f"          -> {ingrediente}")
    print("-" * 40)


def menu():
    """Função principal que exibe o menu e processa as opções."""
    while True:
        print("\n" + "=" * 25)
        print("🍔 Montador de Sanduíche (Pilha)")
        print("=" * 25)
        print("1 - Adicionar ingrediente")
        print("2 - Remover ingrediente (do topo)")
        print("3 - Ver último ingrediente adicionado")
        print("4 - Mostrar sanduíche")
        print("5 - Finalizar pedido")
        print("-" * 25)

        try:
            opcao = input("Digite a opção desejada: ")
            
            if opcao == '1':
                ingrediente = input("Informe o nome do ingrediente a adicionar: ")
                adicionar_ingrediente(ingrediente)
            
            elif opcao == '2':
                remover_ingrediente()
            
            elif opcao == '3':
                ver_ultimo_ingrediente()
            
            elif opcao == '4':
                mostrar_sanduiche()
            
            elif opcao == '5':
                print("\n👋 Pedido finalizado. Bom apetite!")
                break  # Encerra o loop e o programa
            
            else:
                print("\n❌ Opção inválida. Por favor, escolha um número de 1 a 5.")

        except ValueError:
            print("\n❌ Entrada inválida. Por favor, insira um número.")

# Executa o menu principal
if __name__ == "__main__":
    menu()