from professor import Professor
from aluno import Aluno
from curso_idioma import CursoIdioma

class PlataformaIdiomas:
    """Plataforma central que agrega professores, alunos e cursos (AGREGAÇÃO)."""
    def __init__(self, nome: str):
        self.nome = nome
        # AGREGAÇÃO: As listas contêm objetos que existem de forma independente
        self.professores: list[Professor] = []
        self.alunos: list[Aluno] = []
        self.cursos: list[CursoIdioma] = []

    def cadastrar_professor(self, professor: Professor):
        self.professores.append(professor)

    def cadastrar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def adicionar_curso(self, curso: CursoIdioma):
        self.cursos.append(curso)

    def listar_professores(self) -> str:
        if not self.professores:
            return "Nenhum professor cadastrado."
        return "\n".join([f"  {idx+1}. {p}" for idx, p in enumerate(self.professores)])

    def listar_alunos(self) -> str:
        if not self.alunos:
            return "Nenhum aluno cadastrado."
        return "\n".join([f"  {idx+1}. {a}" for idx, a in enumerate(self.alunos)])

    def listar_cursos(self) -> str:
        if not self.cursos:
            return "Nenhum curso cadastrado."
        return "\n".join([f"  {idx+1}. {c}" for idx, c in enumerate(self.cursos)])