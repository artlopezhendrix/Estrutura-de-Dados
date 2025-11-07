def main():
    fila = []
    
    print("=== SIMULADOR DE FILA DE ATENDIMENTO ===")
    print("Programa iniciado! Use o menu abaixo:\n")
    
    while True:
        print("\n" + "-" * 30)
        print("MENU PRINCIPAL")
        print("-" * 30)
        print("1 - Adicionar pessoa à fila")
        print("2 - Atender pessoa")
        print("3 - Mostrar fila")
        print("4 - Sair")
        print("-" * 30)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            nome = input("Digite o nome da pessoa: ").strip()
            if nome:
                fila.append(nome)
                print(f"✓ '{nome}' adicionado(a) ao final da fila!")
                print(f"Posição na fila: {len(fila)}º")
            else:
                print("✗ Nome inválido!")
                
        elif opcao == "2":
            if fila:
                pessoa_atendida = fila.pop(0)
                print(f"✓ Atendendo: {pessoa_atendida}")
                if fila:
                    print(f"Próximo da fila: {fila[0]}")
                else:
                    print("✓ Fila esvaziada!")
            else:
                print("✗ Fila vazia! Ninguém para atender.")
                
        elif opcao == "3":
            if fila:
                print("\n--- FILA ATUAL ---")
                for i, pessoa in enumerate(fila, 1):
                    print(f"{i}º - {pessoa}")
                print(f"Total: {len(fila)} pessoa(s) na fila")
            else:
                print("✗ Fila vazia!")
                
        elif opcao == "4":
            print("\n=== PROGRAMA ENCERRADO ===")
            if fila:
                print(f"Pessoas restantes na fila: {len(fila)}")
            print("Obrigado por usar o simulador!")
            break
            
        else:
            print("✗ Opção inválida! Digite 1, 2, 3 ou 4.")

# Executar o programa
if __name__ == "__main__":
    main()