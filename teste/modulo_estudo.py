from licao import Licao

class ModuloEstudo:
    """Faz parte do ciclo de vida de um CursoIdioma (COMPOSIÇÃO)."""
    def __init__(self, titulo: str, ordem: int):
        self.titulo = titulo
        self.ordem = ordem
        self.licoes: list[Licao] = []

    def adicionar_licao(self, licao: Licao):
        self.licoes.append(licao)

    def calcular_duracao_total(self) -> int:
        return sum(l.obter_duracao_estimada() for l in self.licoes)

    def __str__(self):
        duracao = self.calcular_duracao_total()
        return f"Módulo {self.ordem}: {self.titulo} ({len(self.licoes)} lições, ~{duracao} min)"