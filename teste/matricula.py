from datetime import datetime
from aluno import Aluno
from curso_idioma import CursoIdioma

class Matricula:
    """Conecta um Aluno a um CursoIdioma (ASSOCIAÇÃO SIMPLES)."""
    def __init__(self, aluno: Aluno, curso: CursoIdioma):
        self.aluno = aluno
        self.curso = curso
        self.data_matricula = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.progresso_percentual = 0.0

    def atualizar_progresso(self, novo_percentual: float):
        self.progresso_percentual = min(100.0, max(0.0, novo_percentual))

    def __str__(self):
        return f"Matrícula [{self.data_matricula}] | Aluno: {self.aluno.nome} -> Idioma: {self.curso.idioma} ({self.curso.nome}) | Progresso: {self.progresso_percentual:.1f}%"