class Aluno:
    def __init__(self, nome: str, email: str, nivel_conhecimento: str = "Iniciante"):
        self.nome = nome
        self.email = email
        self.nivel_conhecimento = nivel_conhecimento

    def __str__(self):
        return f"Aluno: {self.nome} <{self.email}> [Nível geral: {self.nivel_conhecimento}]"