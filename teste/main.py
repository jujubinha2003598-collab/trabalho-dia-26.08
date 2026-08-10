from plataforma import PlataformaIdiomas
from professor import Professor
from aluno import Aluno
from curso_idioma import CursoIdioma
from licao_gramatica import LicaoGramatica
from licao_vocabulario import LicaoVocabulario
from licao_audio import LicaoAudio
from matricula import Matricula

def popular_dados_iniciais(plataforma: PlataformaIdiomas):
    """Pré-carrega o sistema com cursos de 2 IDIOMAS (Inglês e Espanhol)."""
    # 1. Professores
    prof_ingles = Professor("John Smith", ["Inglês"], "Estados Unidos")
    prof_espanhol = Professor("Maria Garcia", ["Espanhol"], "Espanha")
    plataforma.cadastrar_professor(prof_ingles)
    plataforma.cadastrar_professor(prof_espanhol)

    # 2. Aluno inicial
    aluno1 = Aluno("Lucas Silva", "lucas@email.com", "Intermediário")
    plataforma.cadastrar_aluno(aluno1)

    # 3. IDIOMA 1: Curso de Inglês
    curso_en = CursoIdioma("English for Everyday Life", "Inglês", prof_ingles)
    mod1_en = curso_en.criar_modulo("Basics & Introductions")
    mod1_en.adicionar_licao(LicaoGramatica("Verb To Be & Personal Pronouns", "Básico", "Verb To Be", 5))
    mod1_en.adicionar_licao(LicaoVocabulario("Greetings & Daily Words", "Básico", 20))
    mod1_en.adicionar_licao(LicaoAudio("Ordering Coffee in NY", "Básico", 3, True))

    # 4. IDIOMA 2: Curso de Espanhol
    curso_es = CursoIdioma("Español Interactivo y Fluidez", "Espanhol", prof_espanhol)
    mod1_es = curso_es.criar_modulo("Presente de Indicativo y Saludos")
    mod1_es.adicionar_licao(LicaoGramatica("Verbos Regulares en Presente", "Básico", "Conjugación de verbos -ar, -er, -ir", 6))
    mod1_es.adicionar_licao(LicaoVocabulario("Vocabulario de la Ciudad y Viajes", "Básico", 25))
    mod1_es.adicionar_licao(LicaoAudio("Entrevista en Madrid", "Intermediário", 4, False))

    plataforma.adicionar_curso(curso_en)
    plataforma.adicionar_curso(curso_es)

    # 5. Matrículas do mesmo aluno nos 2 IDIOMAS
    m1 = Matricula(aluno1, curso_en)
    m1.atualizar_progresso(35.0)
    m2 = Matricula(aluno1, curso_es)
    m2.atualizar_progresso(15.0)

    return [m1, m2]

def exibir_menu():
    print("\n" + "=" * 55)
    print("      PLATAFORMA DE CURSOS DE IDIOMAS (2 IDIOMAS)      ")
    print("=" * 55)
    print("1. Listar Professores Agregados (Agregação)")
    print("2. Listar Alunos Cadastrados")
    print("3. Listar Cursos de Idiomas Disponíveis")
    print("4. Cadastrar Novo Professor ou Aluno")
    print("5. Criar Novo Curso de Idioma (Composição de Módulos)")
    print("6. Adicionar Lição a um Módulo (Herança & Polimorfismo)")
    print("7. Matricular Aluno em Curso (Associação Simples)")
    print("8. Praticar Lição de Idioma (Polimorfismo em Ação)")
    print("9. Ver Matrículas e Progresso nos 2 Idiomas")
    print("0. Sair")
    print("=" * 55)

def main():
    plataforma = PlataformaIdiomas("LinguaWorld - Escola de Idiomas Online")
    matriculas = popular_dados_iniciais(plataforma)

    print(f"\n[INICIALIZAÇÃO] Sistema '{plataforma.nome}' iniciado!")
    print("[INFO] Dados de exemplo pré-carregados com 2 IDIOMAS (Inglês e Espanhol).")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print(f"\n--- PROFESSORES CADASTRADOS ({plataforma.nome}) ---")
            print(plataforma.listar_professores())

        elif opcao == "2":
            print(f"\n--- ALUNOS CADASTRADOS ---")
            print(plataforma.listar_alunos())

        elif opcao == "3":
            print(f"\n=== CURSOS DE IDIOMAS DISPONÍVEIS ===")
            for c in plataforma.cursos:
                print(f"\n> {c}")
                for mod in c.modulos:
                    print(f"   └─ {mod}")
                    for licao in mod.licoes:
                        print(f"       • {licao}")

        elif opcao == "4":
            sub = input("Deseja cadastrar (1) Professor ou (2) Aluno? ").strip()
            if sub == "1":
                nome = input("Nome do Professor: ").strip()
                idiomas_input = input("Idiomas ministrados (separados por vírgula): ").strip()
                idiomas = [i.strip() for i in idiomas_input.split(",")]
                pais = input("País de origem: ").strip()
                prof = Professor(nome, idiomas, pais)
                plataforma.cadastrar_professor(prof)
                print(f"\n[SISTEMA] Professor {nome} cadastrado!")
            elif sub == "2":
                nome = input("Nome do Aluno: ").strip()
                email = input("E-mail: ").strip()
                nivel = input("Nível (Iniciante/Intermediário/Avançado): ").strip()
                aluno = Aluno(nome, email, nivel)
                plataforma.cadastrar_aluno(aluno)
                print(f"\n[SISTEMA] Aluno {nome} cadastrado com sucesso!")

        elif opcao == "5":
            if not plataforma.professores:
                print("\n[ERRO] Cadastre ao menos um professor primeiro.")
                continue
            print("\nSelecione o Professor responsável:")
            print(plataforma.listar_professores())
            idx_p = int(input("Número: ")) - 1
            prof = plataforma.professores[idx_p]

            idioma = input("Idioma do Curso (ex: Francês, Italiano, Alemão): ").strip()
            nome_c = input("Nome do Curso: ").strip()
            curso = CursoIdioma(nome_c, idioma, prof)

            qtd_mod = int(input("Quantos módulos deseja criar inicialmente? "))
            for i in range(qtd_mod):
                t_mod = input(f"  Título do Módulo {i+1}: ").strip()
                curso.criar_modulo(t_mod)

            plataforma.adicionar_curso(curso)
            print(f"\n[SISTEMA] Curso de {idioma} '{nome_c}' criado com sucesso!")

        elif opcao == "6":
            if not plataforma.cursos:
                print("\n[ERRO] Nenhum curso cadastrado.")
                continue

            print("\nSelecione o Curso de Idioma:")
            print(plataforma.listar_cursos())
            idx_c = int(input("Número do curso: ")) - 1
            curso = plataforma.cursos[idx_c]

            if not curso.modulos:
                print("\n[ERRO] Este curso não possui módulos.")
                continue

            print("\nSelecione o Módulo:")
            for idx, m in enumerate(curso.modulos):
                print(f"  {idx+1}. {m.titulo}")
            idx_m = int(input("Número do módulo: ")) - 1
            modulo = curso.modulos[idx_m]

            print("\nTipo de Lição:")
            print("1. Lição de Gramática")
            print("2. Lição de Vocabulário")
            print("3. Lição de Áudio e Pronúncia (Listening)")
            tipo = input("Opção: ").strip()

            titulo_l = input("Título da Lição: ").strip()
            nivel_l = input("Nível (Básico/Intermediário/Avançado): ").strip()

            if tipo == "1":
                regra = input("Regra Gramatical principal: ").strip()
                qtd_ex = int(input("Quantidade de exercícios: "))
                licao = LicaoGramatica(titulo_l, nivel_l, regra, qtd_ex)
            elif tipo == "2":
                qtd_p = int(input("Quantidade de novas palavras: "))
                licao = LicaoVocabulario(titulo_l, nivel_l, qtd_p)
            elif tipo == "3":
                dur = int(input("Duração do áudio em minutos: "))
                trans = input("Possui transcrição? (s/n): ").strip().lower() == 's'
                licao = LicaoAudio(titulo_l, nivel_l, dur, trans)
            else:
                print("\n[ERRO] Tipo inválido.")
                continue

            modulo.adicionar_licao(licao)
            print(f"\n[SISTEMA] Lição '{titulo_l}' adicionada! Tempo estimado: {licao.obter_duracao_estimada()} min.")

        elif opcao == "7":
            if not plataforma.alunos or not plataforma.cursos:
                print("\n[ERRO] É necessário ter pelo menos 1 aluno e 1 curso cadastrados.")
                continue

            print("\nSelecione o Aluno:")
            print(plataforma.listar_alunos())
            idx_a = int(input("Número: ")) - 1

            print("\nSelecione o Curso de Idioma:")
            print(plataforma.listar_cursos())
            idx_c = int(input("Número: ")) - 1

            aluno = plataforma.alunos[idx_a]
            curso = plataforma.cursos[idx_c]

            mat = Matricula(aluno, curso)
            matriculas.append(mat)
            print(f"\n[SISTEMA] Aluno {aluno.nome} matriculado no curso de {curso.idioma} com sucesso!")

        elif opcao == "8":
            if not plataforma.cursos:
                print("\n[ERRO] Nenhum curso cadastrado.")
                continue

            print("\nSelecione o Curso de Idioma:")
            print(plataforma.listar_cursos())
            idx_c = int(input("Número do curso: ")) - 1
            curso = plataforma.cursos[idx_c]

            licoes_disponiveis = []
            for m in curso.modulos:
                for l in m.licoes:
                    licoes_disponiveis.append((m, l))

            if not licoes_disponiveis:
                print("\n[AVISO] Nenhuma lição cadastrada neste curso.")
                continue

            print("\nLições disponíveis para prática:")
            for idx, (m, l) in enumerate(licoes_disponiveis):
                print(f"  {idx+1}. [{m.titulo}] {l}")

            idx_l = int(input("Escolha a lição para praticar: ")) - 1
            _, licao_escolhida = licoes_disponiveis[idx_l]

            print("\n" + "~" * 50)
            print("   EXECUTANDO PRÁTICA DA LIÇÃO (POLIMORFISMO)   ")
            print("~" * 50)
            print(f"Resultado: {licao_escolhida.executar_licao()}")
            print(f"Duração estimada de estudo: {licao_escolhida.obter_duracao_estimada()} minutos.")
            print("~" * 50)

        elif opcao == "9":
            print("\n=== MATRÍCULAS E PROGRESSO DOS ALUNOS ===")
            if not matriculas:
                print("Nenhuma matrícula realizada.")
            for mat in matriculas:
                print(f"- {mat}")

        elif opcao == "0":
            print("\nEncerrando o sistema de idiomas...")
            break
        else:
            print("\n[ERRO] Opção inválida.")

if __name__ == "__main__":
    main()