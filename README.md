## Tratamento das Tabelas Alunos e Matricula e Cruzamento dos Dados
realizamos o tratamento preliminar das tabelas Alunos e Matricula, com o objetivo de preparar os dados para análise e posterior cruzamento. As seguintes ações foram executadas:

Remoção de colunas totalmente vazias;

Eliminação de dados considerados irrelevantes para a análise;

Padronização de nomes e tipos de dados quando necessário.

Cruzamento das Tabelas
O cruzamento dos datasets foi feito com base na correspondência entre os campos:

aluno na tabela Matricula

id_aluno na tabela Alunos

A junção foi realizada utilizando a técnica de merge com chave de igualdade entre esses dois campos.

Considerações sobre Dados Repetidos
Durante o processo, identificamos a presença de múltiplos registros com o mesmo id_aluno, o que indicava que um mesmo aluno poderia estar vinculado a mais de um curso. No entanto, como a tabela de cursos estava oculta, optamos por não considerar essa possibilidade no momento. Com isso, a tabela resultante da junção contemplou aproximadamente 750 alunos únicos.
