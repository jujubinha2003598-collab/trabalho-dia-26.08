from     import
from     import
from     import

class PlataformaIdiomas:
 def __init__(self, nome: str):
        self.nome = nome
        self.professores: list[Professor] = []
        self.alunos: list[Aluno] = []

def popular_dados_iniciais(plataforma: PlataformaIdiomas):


    coord = Coordenador("Dra. Helena Souza", "helena@linguaworld.com", "Coordenação Geral")
    plataforma.cadastrar_coordenador(coord)

    prof_ingles = Professor("John Smith", ["Inglês"], "Estados Unidos")
    prof_italiano = Professor("Giulia Bianchi", ["Italiano"], "Itália")
    plataforma.cadastrar_professor(prof_ingles)
    plataforma.cadastrar_professor(prof_italiano)

    aluno1 = Aluno("Lucas Silva", "lucas@email.com", "Intermediário")
    plataforma.cadastrar_aluno(aluno1)

    curso_en = CursoIdioma("English Fluency Program", "Inglês", prof_ingles)
    mod_en_basico = curso_en.criar_modulo("Level 1: Essential English")
    perguntas_en_basico = [
        {
            "pergunta": "How do you say 'Olá, como você está?' in English?",
            "opcoes": ["A) Goodbye, see you!", "B) Hello, how are you?", "C) Good night, my friend.", "D) What is your name?"],
            "resposta": "B"
        },
        {
            "pergunta": "Complete with Verb To Be: 'She ___ a brilliant student.'",
            "opcoes": ["A) am", "B) are", "C) is", "D) be"],
            "resposta": "C"
        },
        {
            "pergunta": "Which personal pronoun replaces 'Lucas and Maria'?",
            "opcoes": ["A) We", "B) They", "C) You", "D) He"],
            "resposta": "B"
        },
        {
            "pergunta": "What is the opposite of 'hot'?",
            "opcoes": ["A) Warm", "B) Dry", "C) Cold", "D) Fast"],
            "resposta": "C"
        },
        {
            "pergunta": "Translate: 'Eu gostaria de um café, por favor.'",
            "opcoes": ["A) I want coffee now.", "B) I would like a coffee, please.", "C) Can I get tea?", "D) Coffee is good."],
            "resposta": "B"
        }
    ]
    mod_en_basico.adicionar_licao(
        LicaoGramatica("Verb To Be & Greetings", "Básico", "Verb To Be", 5, perguntas_en_basico)
    )

    mod_en_inter = curso_en.criar_modulo("Level 2: Intermediate Communication")
    perguntas_en_inter = [
        {
            "pergunta": "Complete with Present Perfect: 'I ___ in this city since 2020.'",
            "opcoes": ["A) lived", "B) have lived", "C) am living", "D) live"],
            "resposta": "B"
        },
        {
            "pergunta": "Which preposition is correct: 'She is very interested ___ art.'?",
            "opcoes": ["A) on", "B) at", "C) in", "D) with"],
            "resposta": "C"
        },
        {
            "pergunta": "What does the phrasal verb 'give up' mean?",
            "opcoes": ["A) Entregar algo", "B) Desistir", "C) Continuar tentando", "D) Levantar"],
            "resposta": "B"
        },
        {
            "pergunta": "Choose the correct sentence in Second Conditional:",
            "opcoes": [
                "A) If I had money, I will buy a car.",
                "B) If I have money, I bought a car.",
                "C) If I were you, I would study more.",
                "D) If I am you, I would go."
            ],
            "resposta": "C"
        },
        {
            "pergunta": "What is the past simple form of 'teach'?",
            "opcoes": ["A) Teached", "B) Taught", "C) Thought", "D) Teaching"],
            "resposta": "B"
        }
    ]
    mod_en_inter.adicionar_licao(
        LicaoVocabulario("Phrasal Verbs & Tenses", "Intermediário", 25, perguntas_en_inter)
    )

    mod_en_adv = curso_en.criar_modulo("Level 3: Advanced & Business English")
    perguntas_en_adv = [
        {
            "pergunta": "Complete using inversion: 'Hardly ___ when the meeting started.'",
            "opcoes": ["A) had I arrived", "B) I had arrived", "C) I arrived", "D) did I arrived"],
            "resposta": "A"
        },
        {
            "pergunta": "What does the idiom 'barking up the wrong tree' mean?",
            "opcoes": ["A) Latir para o cachorro certo", "B) Estar enganado sobre a causa de algo", "C) Subir em uma árvore", "D) Trabalhar rápido"],
            "resposta": "B"
        },
        {
            "pergunta": "'I regret ___ you that the event was canceled.' Fill in the blank:",
            "opcoes": ["A) to inform", "B) informing", "C) inform", "D) informed"],
            "resposta": "A"
        },
        {
            "pergunta": "Which word means 'subtilmente' in formal English?",
            "opcoes": ["A) Strongly", "B) Subtly", "C) Loudly", "D) Unlikely"],
            "resposta": "B"
        },
        {
            "pergunta": "Translate: 'Se eu soubesse da reunião, teria comparecido.'",
            "opcoes": [
                "A) If I knew about the meeting, I came.",
                "B) Had I known about the meeting, I would have attended.",
                "C) If I know the meeting, I would attend.",
                "D) When I knew the meeting, I attended."
            ],
            "resposta": "B"
        }
    ]
    mod_en_adv.adicionar_licao(
        LicaoAudio("Business Negotiation & Idioms", "Avançado", 5, True, perguntas_en_adv)
    )

    curso_it = CursoIdioma("Corso di Lingua Italiana", "Italiano", prof_italiano)


    mod_it_basico = curso_it.criar_modulo("Livello 1: Primi Passi in Italiano")
    perguntas_it_basico = [
        {
            "pergunta": "Como se diz 'Bom dia' em italiano?",
            "opcoes": ["A) Buonasera", "B) Buongiorno", "C) Buonanotte", "D) Ciao ragazzi"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o artigo definido masculino singular correto para 'ragazzo'?",
            "opcoes": ["A) La", "B) Lo", "C) Il", "D) L'"],
            "resposta": "C"
        },
        {
            "pergunta": "Traduza: 'Come ti chiami?'",
            "opcoes": ["A) De onde você é?", "B) Como você se chama?", "C) Quantos anos você tem?", "D) Onde você mora?"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o plural da palavra 'gelato'?",
            "opcoes": ["A) Gelati", "B) Gelate", "C) Gelatos", "D) Gelaten"],
            "resposta": "A"
        },
        {
            "pergunta": "Conjugue o verbo 'essere' para 'io':",
            "opcoes": ["A) io sei", "B) io è", "C) io sono", "D) io siamo"],
            "resposta": "C"
        }
    ]
    mod_it_basico.adicionar_licao(
        LicaoGramatica("Verbo Essere e Saluti", "Básico", "Coniugazione Essere", 5, perguntas_it_basico)
    )

    mod_it_inter = curso_it.criar_modulo("Livello 2: Conversazione e Viaggi")
    perguntas_it_inter = [
        {
            "pergunta": "Qual é a forma correta do Passato Prossimo do verbo 'andare' para 'noi'?",
            "opcoes": ["A) abbiamo andato", "B) siamo andati", "C) sono andato", "D) avete andato"],
            "resposta": "B"
        },
        {
            "pergunta": "Traduza: 'Gostaria de reservar uma mesa para duas pessoas.'",
            "opcoes": [
                "A) Vorrei prenotare un tavolo per due persone.",
                "B) Voglio mangiare con due persone.",
                "C) Posso ordinare per due?",
                "D) Mi piace il tavolo due."
            ],
            "resposta": "A"
        },
        {
            "pergunta": "O que significa a partícula 'ci' na frase 'Ci vado domani'?",
            "opcoes": ["A) Nós", "B) Lá / A esse lugar", "C) Comigo", "D) Nada"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual palavra indica excesso ('demais') em italiano?",
            "opcoes": ["A) Molto", "B) Troppo", "C) Poco", "D) Abbastanza"],
            "resposta": "B"
        },
        {
            "pergunta": "Como fica a combinação do pronome 'mi' + 'lo'?",
            "opcoes": ["A) milo", "B) me lo", "C) lo mi", "D) glielo"],
            "resposta": "B"
        }
    ]
    mod_it_inter.adicionar_licao(
        LicaoVocabulario("Viaggi e Ristorante", "Intermediário", 30, perguntas_it_inter)
    )

  
    mod_it_adv = curso_it.criar_modulo("Livello 3: Fluente e Letteratura")
    perguntas_it_adv = [
        {
            "pergunta": "Qual modo verbal exprime dúvida, opinião ou desejo em italiano?",
            "opcoes": ["A) Indicativo", "B) Imperativo", "C) Congiuntivo", "D) Condizionale"],
            "resposta": "C"
        },
        {
            "pergunta": "Complete com o Congiuntivo: 'Spero che tu ___ un buon viaggio.'",
            "opcoes": ["A) fai", "B) faccia", "C) fatto", "D) fare"],
            "resposta": "B"
        },
        {
            "pergunta": "O que significa a expressão 'In bocca al lupo!'?",
            "opcoes": ["A) Cuidado com o perigo", "B) Boa sorte!", "C) Cuidado com o lobo", "D) Bom apetite!"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual conjunção significa 'Embora / Apesar de' em italiano?",
            "opcoes": ["A) Perché", "B) Sebbene", "C) Quindi", "D) Inoltre"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual tempo verbal é usado em narrativas históricas ou literárias distantes?",
            "opcoes": ["A) Passato Prossimo", "B) Passato Remoto", "C) Imperfetto", "D) Futuro Anteriore"],
            "resposta": "B"
        }
    ]
    mod_it_adv.adicionar_licao(
        LicaoAudio("Cultura e Congiuntivo", "Avançado", 6, False, perguntas_it_adv)
    )

    plataforma.adicionar_curso(curso_en)
    plataforma.adicionar_curso(curso_it)


    m1 = Matricula(aluno1, curso_en)
    m1.atualizar_progresso(40.0)
    m2 = Matricula(aluno1, curso_it)
    m2.atualizar_progresso(20.0)

    return [m1, m2]


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
