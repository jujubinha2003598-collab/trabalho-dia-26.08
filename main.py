from plataforma import PlataformaIdiomas
from professor import Professor
from aluno import Aluno
from curso_idioma import CursoIdioma
from licao_gramatica import LicaoGramatica
from licao_vocabulario import LicaoVocabulario
from matricula import Matricula








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

if __name__ == "__main__":
    main()