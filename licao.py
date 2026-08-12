from abc import ABC, abstractmethod

class Licao(ABC):
    def __init__(self, titulo: str, nivel: str, perguntas: list[dict] = None):
        self.titulo = titulo
        self.nivel = nivel 
        self.perguntas = perguntas if perguntas is not None else []

    @abstractmethod
    def obter_duracao_estimada(self) -> int:
        pass

    @abstractmethod
    def executar_licao(self) -> str:
        pass

    def executar_quiz(self) -> int:

        if not self.perguntas:
            print("\n   (Sem perguntas cadastradas para esta lição)")
            return 0

        respostas_aluno = []
        total = len(self.perguntas)

        print("\n" + "=" * 55)
        print(f"📝 INICIANDO PROVA: {self.titulo} [{self.nivel}]")
        print("=" * 55)
        for idx, q in enumerate(self.perguntas, 1):
            print(f"\nQuestão {idx}/{total}: {q['pergunta']}")
            for opcao in q['opcoes']:
                print(f"   {opcao}")

            resp = ""
            while resp not in ["A", "B", "C", "D"]:
                resp = input("\n👉 Sua resposta (A, B, C ou D): ").strip().upper()
                if resp not in ["A", "B", "C", "D"]:
                    print("⚠️ Opção inválida! Escolha apenas entre A, B, C ou D.")

            respostas_aluno.append(resp)
            print("-" * 55)
        acertos = 0
        print("\n" + "=" * 60)
        print("📊 GABARITO E CORREÇÃO DA PROVA")
        print("=" * 60)

        for idx, (q, resp_aluno) in enumerate(zip(self.perguntas, respostas_aluno), 1):
            resp_correta = q['resposta'].upper()

            if resp_aluno == resp_correta:
                acertos += 1
                print(f"Questão {idx}: ✅ ACERTOU! (Sua resposta: {resp_aluno})")
            else:
                print(f"Questão {idx}: ❌ ERROU! (Sua resposta: {resp_aluno} | Gabarito Correto: {resp_correta})")

        aproveitamento = int((acertos / total) * 100)
        print("=" * 60)
        print(f"🎯 NOTA FINAL: {acertos} de {total} acertos ({aproveitamento}% de aproveitamento)")
        print("=" * 60)

        return acertos

    def __str__(self):
        return f"Lição: {self.titulo} [{self.nivel}] ({len(self.perguntas)} perguntas)"