import pandas as pd

# Lê o Excel
alunos = pd.read_excel("alunos_pii_tratado.xlsx")

# Padroniza nomes das colunas: minúsculo, sem espaços, sem acentos
alunos.columns = alunos.columns.str.strip().str.lower().str.replace(" ", "_")

# Agora a coluna virou 'id_aluno'

# Converte para número inteiro sem notação científica
alunos["id_aluno"] = pd.to_numeric(alunos["id_aluno"], errors="coerce").astype("Int64")

# Converte para string se quiser garantir sem notação científica
alunos["id_aluno"] = alunos["id_aluno"].astype(str)

# Verifica duplicados
duplicados = alunos[alunos.duplicated(subset="id_aluno", keep=False)]
print("\n🔁 IDs duplicados:")
print(duplicados.sort_values("id_aluno"))

# Remove duplicados (mantém o primeiro)
alunos = alunos.drop_duplicates(subset="id_aluno", keep="first")

alunos = alunos.dropna(axis=1, how='all')


# Salva se quiser
alunos.to_excel("alunos_tratado_sem_duplicatas.xlsx", index=False)
