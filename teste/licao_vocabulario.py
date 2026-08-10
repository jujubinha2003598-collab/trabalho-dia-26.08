from licao import Licao

class LicaoVocabulario(Licao):
    """Subclasse para lições de ampliação de vocabulário e flashcards (HERANÇA)."""
    def __init__(self, titulo: str, nivel: str, qtd_palavras: int):
        super().__init__(titulo, nivel)
        self.qtd_palavras = qtd_palavras

    def obter_duracao_estimada(self) -> int:
        # Estima ~1.2 minutos por palavra em sistema de repetição espaçada
        return max(5, round(self.qtd_palavras * 1.2))

    def executar_licao(self) -> str:
        return f"🪪 [Vocabulário - {self.nivel}] Prática de memorização e flashcards com {self.qtd_palavras} novas palavras."