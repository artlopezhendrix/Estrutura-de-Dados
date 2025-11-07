class FilaImpressao:
    """
    Simula uma fila de impressão usando a lista padrão do Python.
    """
    def __init__(self):
        # A lista (list) é usada para armazenar os itens da fila
        self.trabalhos = []

    def adicionar_trabalho(self, nome_trabalho):
        """Adiciona um trabalho de impressão (enqueue) ao final da fila."""
        # Usamos append() para adicionar ao final (direita) da lista.
        self.trabalhos.append(nome_trabalho)
        print(f"✅ Adicionado: '{nome_trabalho}'.")

    def processar_trabalho(self):
        """
        Processa (remove) o trabalho mais antigo (dequeue) da fila.
        Usa pop(0) para o comportamento FIFO.
        """
        if self.esta_vazia():
            print("⚠️ Fila de impressão vazia. Nenhum trabalho para processar.")
            return None
        else:
            # pop(0) remove o primeiro elemento (índice 0), garantindo FIFO.
            trabalho_processado = self.trabalhos.pop(0)
            print(f"🖨️ Processando: '{trabalho_processado}'.")
            return trabalho_processado

    def esta_vazia(self):
        """Verifica se a fila não tem trabalhos pendentes."""
        return len(self.trabalhos) == 0

    def ver_proximo(self):
        """Visualiza, sem remover, o próximo trabalho a ser processado."""
        if self.esta_vazia():
            print("A fila está vazia.")
            return None
        else:
            return self.trabalhos[0]

# --- Demonstração de Uso ---

# 1. Cria a fila de impressão
impressora_fila = FilaImpressao()

print("--- Inicializando Fila de Impressão ---")

# 2. Adiciona trabalhos à fila
impressora_fila.adicionar_trabalho("Relatório Mensal")
impressora_fila.adicionar_trabalho("Foto de Capa")
impressora_fila.adicionar_trabalho("Currículo da Maria")

# 3. Verifica o próximo trabalho
proximo = impressora_fila.ver_proximo()
print(f"\n👀 Próximo na fila: {proximo}")

# 4. Processa os dois primeiros trabalhos
print("\n--- Iniciando Processamento ---")
impressora_fila.processar_trabalho()  # Processa "Relatório Mensal"
impressora_fila.processar_trabalho()  # Processa "Foto de Capa"

# 5. Adiciona um trabalho urgente
impressora_fila.adicionar_trabalho("Nota Fiscal Urgente")

# 6. Processa o restante da fila
impressora_fila.processar_trabalho()  # Processa "Currículo da Maria"
impressora_fila.processar_trabalho()  # Processa "Nota Fiscal Urgente"

# 7. Tenta processar a fila vazia
impressora_fila.processar_trabalho()