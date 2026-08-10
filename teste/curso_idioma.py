from modulo_estudo import ModuloEstudo
from professor import Professor

class CursoIdioma:
    """Curso específico de um idioma (ex: Inglês, Espanhol). Gerencia seus Módulos (COMPOSIÇÃO)."""
    def __init__(self, nome: str, idioma: str, professor: Professor):
        self.nome = nome
        self.idioma = idioma
        self.professor = professor
        # COMPOSIÇÃO: Módulos pertencem exclusivamente a este curso
        self.modulos: list[ModuloEstudo] = []

    def criar_modulo(self, titulo_modulo: str) -> ModuloEstudo:
        ordem = len(self.modulos) + 1
        modulo = ModuloEstudo(titulo_modulo, ordem)
        self.modulos.append(modulo)
        return modulo

    def calcular_duracao_total(self) -> int:
        return sum(m.calcular_duracao_total() for m in self.modulos)

    def __str__(self):
        duracao = self.calcular_duracao_total()
        return f"Curso de {self.idioma}: '{self.nome}' | {self.professor.nome} | {len(self.modulos)} Módulo(s) | Carga Total: ~{duracao} min"