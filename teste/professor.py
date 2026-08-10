class Professor:
    """Representa um instrutor especialista (AGREGAÇÃO com Plataforma)."""
    def __init__(self, nome: str, idiomas_ministrados: list[str], pais_origem: str):
        self.nome = nome
        self.idiomas_ministrados = idiomas_ministrados
        self.pais_origem = pais_origem

    def __str__(self):
        idiomas = ", ".join(self.idiomas_ministrados)
        return f"Prof. {self.nome} ({self.pais_origem}) | Idiomas: {idiomas}"