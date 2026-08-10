# trabalho-dia-26.08

    Plataforma de Cursos Online (LMS)
Herança & Polimorfismo: Classe base Conteudo com subclasses VideoAula, ArtigoTexto e Quiz. O método obter_duracao_estimada() ou validar_conclusao() funciona de forma única para cada formato.

Composição: O Curso possui seus Modulos. Se o curso for deletado, os módulos pertencentes a ele são deletados junto.

Agregação: A Plataforma agrega Professores (o professor existe independentemente de ter ou não um curso ativo no momento).

Associação Simples: A Inscricao conecta um Aluno a um Curso.
