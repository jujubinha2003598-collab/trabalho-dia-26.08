from licao import Licao

class LicaoGramatica(Licao):
    """Subclasse para lições focadas em regras gramaticais e escrita (HERANÇA)."""
    def __init__(self, titulo: str, nivel: str, regra_principal: str, qtd_exercicios: int):
        super().__init__(titulo, nivel)
        self.regra_principal = regra_principal
        self.qtd_exercicios = qtd_exercicios

    def obter_duracao_estimada(self) -> int:
        # Estima 10 min de teoria + 4 minutos por exercício gramatical
        return 10 + (self.qtd_exercicios * 4)

    def executar_licao(self) -> str:
        return f"📖 [Gramática - {self.nivel}] Estudo da regra '{self.regra_principal}' com {self.qtd_exercicios} exercícios de escrita."