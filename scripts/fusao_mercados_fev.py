from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'
path_dados_combinados = 'data_processed/dados_combinados.csv'

# Extract
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f"Colunas Arquivo Empresa A: {dados_empresaA.nome_colunas}")
print(f"Qtde de Linhas Empresa A: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f"Colunas Arquivo Empresa B: {dados_empresaB.nome_colunas}")
print(f"Qtde de Linhas Empresa B: {dados_empresaB.qtd_linhas}")

# Transformação
key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Colunas renomeadas Empresa B: {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join_data(dados_empresaA, dados_empresaB)
print(f"Colunas Dados combinados: {dados_fusao.nome_colunas}")
print(f"Qtde de Linhas Dados combinados: {dados_fusao.qtd_linhas}")

# Load
dados_fusao.save_data(path_dados_combinados)
print(f"Dados combinados salvos em: {path_dados_combinados}")
