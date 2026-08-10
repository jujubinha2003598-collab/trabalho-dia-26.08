from abc import ABC, abstractmethod

class Licao(ABC):
    """Classe base abstrata para as lições do curso de idiomas (HERANÇA)."""
    def __init__(self, titulo: str, nivel: str):
        self.titulo = titulo
        self.nivel = nivel  # ex: 'Básico', 'Intermediário', 'Avançado'

    @abstractmethod
    def obter_duracao_estimada(self) -> int:
        """Retorna o tempo estimado em minutos para concluir a lição (POLIMORFISMO)."""
        pass

    @abstractmethod
    def executar_licao(self) -> str:
        """Simula a execução/prática da lição de idioma (POLIMORFISMO)."""
        pass

    def __str__(self):
        return f"Lição: {self.titulo} [{self.nivel}]"