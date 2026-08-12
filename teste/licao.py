from abc import ABC, abstractmethod

class Licao(ABC):
    """Classe base abstrata para as lições do curso de idiomas (HERANÇA)."""
    def __init__(self, titulo: str, nivel: str):
        self.titulo = titulo
        self.nivel = nivel  # ex: 'Básico', 'Intermediário', 'Avançado'

    @abstractmethod
    def obter_duracao_estimada(self) -> int:

        pass

    @abstractmethod
    def executar_licao(self) -> str:

        pass

    def __str__(self):
        return f"Lição: {self.titulo} [{self.nivel}]"