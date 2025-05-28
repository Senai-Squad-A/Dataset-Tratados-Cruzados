import pandas as pd

matricula = pd.read_excel('Matriculas_pii_none.xlsx')

# Padroniza os nomes das colunas
matricula.columns = matricula.columns.str.strip().str.lower().str.replace(" ", "_")

# Converte a coluna 'aluno' para número inteiro (evita notação científica)
matricula["aluno"] = pd.to_numeric(matricula["aluno"], errors="coerce").astype("Int64")

# Converte para string (para preservar e evitar problemas em merges)
matricula["aluno"] = matricula["aluno"].astype(str)

# Remove duplicatas com base na coluna 'aluno', mantendo o primeiro
matricula_sem_duplicatas = matricula.drop_duplicates(subset="aluno", keep="first")

# Salva o resultado em um novo arquivo Excel
matricula_sem_duplicatas.to_excel("matricula_tratada_sem_duplicatas.xlsx", index=False)

matricula = matricula.dropna(axis=1, how='all')

print("✅ Arquivo 'matricula_tratada_sem_duplicatas.xlsx' salvo com sucesso.")
