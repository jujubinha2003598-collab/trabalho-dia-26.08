# trabalho-dia-26.08
4. Sistema de Ingressos e Eventos (Show / Cinema)
Herança & Polimorfismo: Classe base Ingresso com subclasses IngressoPista, IngressoVIP e IngressoCamarote. O método calcular_valor_final() aplica taxas e adicionais conforme a categoria do setor.

Composição: O Evento cria e gerencia o seu MapaDeAssentos (ou programação de horários).

Agregação: A Produtora de eventos agrega uma lista de Artistas / Atracao.

Associação Simples: A Venda vincula um Cliente a um Ingresso.

Algum desses temas se encaixa melhor no que você ou seu grupo estão procurando desenvolver?

3. Plataforma de Cursos Online (LMS)
Herança & Polimorfismo: Classe base Conteudo com subclasses VideoAula, ArtigoTexto e Quiz. O método obter_duracao_estimada() ou validar_conclusao() funciona de forma única para cada formato.

Composição: O Curso possui seus Modulos. Se o curso for deletado, os módulos pertencentes a ele são deletados junto.

Agregação: A Plataforma agrega Professores (o professor existe independentemente de ter ou não um curso ativo no momento).

Associação Simples: A Inscricao conecta um Aluno a um Curso.
