from pathlib import Path
import pandas as pd
import unicodedata
import re

def normalizar(texto):
    texto = str(texto)

    texto = texto.replace('\xa0', ' ')
    texto = texto.strip().upper()

    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')

    texto = re.sub(r'\s+', ' ', texto)

    return texto


pasta_rede = Path(r"Z:\07 - Monitoramento\Controle de Jornada\Arquivo correção de ponto")

arquivo = r"C:\Users\ext.lyncolnSS\Downloads\PASTA DE USO DE TRABALHO\Controle das Pasta da Rede.xlsx"

df = pd.read_excel(arquivo, sheet_name="Motorista")

df.columns = df.columns.astype(str).str.strip().str.upper()

nome_col = "NOME"
status_col = "STATUS NA EMPRESA"

# só ativos
df_ativos = df[df[status_col].astype(str).str.upper() == "ATIVO"]

nomes_planilha = set(normalizar(n) for n in df_ativos[nome_col] if pd.notna(n))

#  AGORA PEGANDO TODAS AS SUBPASTAS (A, B, C... dentro da rede)
pastas_rede = set(
    normalizar(p.name)
    for p in pasta_rede.rglob("*")   # <- AQUI É A CORREÇÃO PRINCIPAL
    if p.is_dir()
    and len(p.name) > 3              # evita pegar só "A", "B", "C"
)

# comparação correta
faltando = sorted(nomes_planilha - pastas_rede)

print("\n🚨 MOTORISTAS SEM PASTA:")
for f in faltando:
    print(f)