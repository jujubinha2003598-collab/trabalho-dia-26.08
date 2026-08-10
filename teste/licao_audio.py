from licao import Licao

class LicaoAudio(Licao):
    """Subclasse para lições de escuta (listening) e pronúncia (HERANÇA)."""
    def __init__(self, titulo: str, nivel: str, duracao_audio_min: int, tem_transcricao: bool):
        super().__init__(titulo, nivel)
        self.duracao_audio_min = duracao_audio_min
        self.tem_transcricao = tem_transcricao

    def obter_duracao_estimada(self) -> int:
        # Áudio ouvido 3 vezes para compreensão e repetição de pronúncia
        return self.duracao_audio_min * 3

    def executar_licao(self) -> str:
        trans = "com transcrição de apoio" if self.tem_transcricao else "sem transcrição (desafio auditivo)"
        return f"🎧 [Listening & Pronúncia - {self.nivel}] Escuta de áudio ({self.duracao_audio_min} min) {trans} e treino de fala."