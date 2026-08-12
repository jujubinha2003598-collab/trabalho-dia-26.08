from plataforma import PlataformaIdiomas
from professor import Professor
from aluno import Aluno
from curso_idioma import CursoIdioma
from licao import Licao
def popular_dados_iniciais(plataforma: PlataformaIdiomas):

    prof_ingles = Professor("John Smith", ["Inglês"], "Estados Unidos")
    prof_espanhol = Professor("Maria Garcia", ["Espanhol"], "Espanha")
    plataforma.cadastrar_professor(prof_ingles)
    plataforma.cadastrar_professor(prof_espanhol)


    aluno1 = Aluno("Lucas Silva", "lucas@email.com", "Intermediário")
    plataforma.cadastrar_aluno(aluno1)


    curso_en = CursoIdioma("English for Everyday Life", "Inglês", prof_ingles)
    mod1_en = curso_en.criar_modulo("Basics & Introductions")
    mod1_en.adicionar_licao(LicaoGramatica("Verb To Be & Personal Pronouns", "Básico", "Verb To Be", 5))
    mod1_en.adicionar_licao(LicaoVocabulario("Greetings & Daily Words", "Básico", 20))
    mod1_en.adicionar_licao(LicaoAudio("Ordering Coffee in NY", "Básico", 3, True))

 

    plataforma.adicionar_curso(curso_en)
    plataforma.adicionar_curso(curso_es)

    m1 = Matricula(aluno1, curso_en)
    m1.atualizar_progresso(35.0)
    m2 = Matricula(aluno1, curso_es)
    m2.atualizar_progresso(15.0)

    return [m1, m2]


def exibir_menu():
    print("\n" + "=" * 55)
    print("      PLATAFORMA DE CURSO INGLÊS E ITALIANO      ")
    print("=" * 55)
    print("1. Listar Professores ")
    print("2. Listar Alunos Cadastrados")
    print("4. Cadastrar Novo Professor ou Aluno")
    print("6. Adicionar Lição a um Módulo ")
    print("7. Matricular Aluno em Curso ")
    print("8. Praticar Lição de Idioma ")
    print("9. Ver Matrículas e Progresso nos Idiomas")
    print("0. Sair")
    print("=" * 55)
def main():
    plataforma = PlataformaIdiomas("LinguaWorld - Inglês & Italiano")
    matriculas = popular_dados_iniciais(plataforma)

    while True:
        print("\n" + "=" * 55)
        print("   LINGUAWORLD - CURSOS DE INGLÊS E ITALIANO   ")
        print("=" * 55)
        print("Quem está acessando?")
        print("1. Coordenador(a)")
        print("2. Professor(a)")
        print("3. Aluno(a)")
        print("0. Sair")
        print("=" * 55)

        perfil = input("Escolha o perfil: ").strip()

        if perfil == "1":
            print("\n--- COORDENADORES CADASTRADOS ---")
            print(plataforma.listar_coordenadores())
            idx = int(input("Selecione seu perfil: ")) - 1
            menu_coordenador(plataforma, matriculas, plataforma.coordenadores[idx])

        elif perfil == "2":
            print("\n--- PROFESSORES CADASTRADOS ---")
            print(plataforma.listar_professores())
            idx = int(input("Selecione seu perfil: ")) - 1
            print(f"\nOlá, Prof. {plataforma.professores[idx].nome}!")

        elif perfil == "3":
            print("\n--- ALUNOS CADASTRADOS ---")
            print(plataforma.listar_alunos())
            idx = int(input("Selecione seu perfil: ")) - 1
            menu_aluno(plataforma, matriculas, plataforma.alunos[idx])

        elif perfil == "0":
            print("\nAté logo!")
            break
def menu_coordenador(plataforma: PlataformaIdiomas, matriculas: list[Matricula], coord: Coordenador):
    while True:
        print("\n" + "=" * 55)
        print(f"    PAINEL DA COORDENAÇÃO - {coord.nome}")
        print("=" * 55)
        print("1. Cadastrar Novo Professor, Aluno ou Coordenador")
        print("2. Criar Novo Curso de Idioma")
        print("3. Matricular Aluno em Curso")
        print("4. Relatório Geral da Plataforma")
        print("5. Ver Todas as Matrículas")
        print("0. Voltar ao Menu Principal")
        print("=" * 55)

        op = input("Opção: ").strip()
        if op == "1":
            tipo = input("Cadastrar (1) Coordenador, (2) Professor ou (3) Aluno: ").strip()
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            if tipo == "1":
                plataforma.cadastrar_coordenador(Coordenador(nome, email, input("Departamento: ")))
            elif tipo == "2":
                idiomas = [i.strip() for i in input("Idiomas (sep. por vírgula): ").split(",")]
                plataforma.cadastrar_professor(Professor(nome, idiomas, input("País: ")))
            elif tipo == "3":
                plataforma.cadastrar_aluno(Aluno(nome, email, input("Nível: ")))
            print(f"\n[SISTEMA] {nome} cadastrado com sucesso!")
        elif op == "4":
            print(f"\n=== RELATÓRIO GERAL: {plataforma.nome} ===")
            print("\n--- COORDENADORES ---")
            print(plataforma.listar_coordenadores())
            print("\n--- PROFESSORES ---")
            print(plataforma.listar_professores())
            print("\n--- ALUNOS ---")
            print(plataforma.listar_alunos())
            print("\n--- CURSOS E LIÇÕES CADASTRADAS ---")
            for c in plataforma.cursos:
                print(f"\n> {c}")
                for mod in c.modulos:
                    print(f"   └─ {mod}")
                    for licao in mod.licoes:
                        print(f"       • {licao}")
        elif op == "5":
            for m in matriculas:
                print(f"- {m}")
        elif op == "0":
            break

def menu_aluno(plataforma: PlataformaIdiomas, matriculas: list[Matricula], aluno: Aluno):
    while True:
        print("\n" + "=" * 55)
        print(f"    PAINEL DO ALUNO - {aluno.nome}")
        print("=" * 55)
        print("1. Ver Cursos de Idiomas (Inglês / Italiano)")
        print("2. Matricular-se em um Curso")
        print("3. Praticar Lição e Responder o Quiz")
        print("4. Minhas Matrículas e Progressos")
        print("0. Voltar ao Menu Principal")
        print("=" * 55)

        op = input("Opção: ").strip()

        if op == "1":
            for c in plataforma.cursos:
                print(f"\n> {c}")
                for mod in c.modulos:
                    print(f"   └─ {mod}")
                    for licao in mod.licoes:
                        print(f"       • {licao}")

        elif op == "2":
            print("\nCursos Disponíveis:")
            print(plataforma.listar_cursos())
            idx_c = int(input("Escolha o curso: ")) - 1
            mat = Matricula(aluno, plataforma.cursos[idx_c])
            matriculas.append(mat)
            print(f"\n[SISTEMA] Matrícula realizada em {plataforma.cursos[idx_c].nome}!")

        elif op == "3":
            print("\nSelecione o Curso de Idioma:")
            print(plataforma.listar_cursos())
            idx_c = int(input("Número do curso: ")) - 1
            curso = plataforma.cursos[idx_c]

            licoes_disponiveis = []
            for m in curso.modulos:
                for l in m.licoes:
                    licoes_disponiveis.append((m, l))

            if not licoes_disponiveis:
                print("\nNenhuma lição disponível.")
                continue

            print("\nLições disponíveis para prática:")
            for idx, (m, l) in enumerate(licoes_disponiveis):
                print(f"  {idx+1}. [{m.titulo}] {l}")

            idx_l = int(input("Escolha a lição: ")) - 1
            mod, licao_escolhida = licoes_disponiveis[idx_l]

            print(f"\nExecutando: {licao_escolhida.executar_licao()}")
            acertos = licao_escolhida.executar_quiz()

            for mat in matriculas:
                if mat.aluno == aluno and mat.curso == curso:
                    ganho_progresso = (acertos / len(licao_escolhida.perguntas)) * 20.0
                    mat.atualizar_progresso(mat.progresso_percentual + ganho_progresso)
                    print(f"[SISTEMA] Seu progresso no curso foi atualizado para {mat.progresso_percentual:.1f}%!")

        elif op == "4":
            minhas = [m for m in matriculas if m.aluno == aluno]
            for m in minhas:
                print(f"- {m}")

        elif op == "0":
            break

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
        from plataforma import PlataformaIdiomas

if __name__ == "__main__":
    main()