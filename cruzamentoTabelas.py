import pandas as pd

# Lê as planilhas
alunos = pd.read_excel('alunos_tratado_sem_duplicatas.xlsx')
matricula = pd.read_excel('matricula_tratada_sem_duplicatas.xlsx')

# Certifique-se de que as colunas têm o mesmo formato (string) e remova espaços extras
alunos["id_aluno"] = alunos["id_aluno"].astype(str).str.strip()
matricula["aluno"] = matricula["aluno"].astype(str).str.strip()

# Verifica os primeiros valores de ambas as colunas para garantir que estão no formato correto
print(alunos["id_aluno"].head())
print(matricula["aluno"].head())

# Cria uma nova coluna indicando se o aluno existe na tabela 'alunos'
matricula["aluno_existe_em_alunos"] = matricula["aluno"].isin(alunos["id_aluno"])

# Verifica os resultados
print(matricula[["aluno", "aluno_existe_em_alunos"]].head())

# (Opcional) Salva o resultado
matricula.to_excel("matricula_com_status.xlsx", index=False)
