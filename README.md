# Pipeline Dados

Este projeto tem como objetivo processar, combinar e analisar dados de diferentes empresas, utilizando arquivos nos formatos JSON e CSV. O pipeline realiza a extração, transformação e fusão do banco de dados de duas empresas, gerando um arquivo consolidado para análises posteriores.

## Case

A Empresa A e a Empresa B passaram por um processo de fusão. Como parte desse processo, o time de engenharia de dados recebeu a tarefa de integrar os bancos de dados das duas empresas, que estavam em formatos distintos (JSON e CSV). O objetivo é entregar uma base de dados única, padronizada e consolidada em formato CSV para o time de análise de dados, facilitando assim a geração de insights e relatórios unificados para a nova organização.

## Estrutura do Projeto

```
.
├── data_raw/
│   ├── dados_empresaA.json
│   └── dados_empresaB.csv
├── data_processed/
│   └── dados_combinados.csv
├── notebooks/
│   └── explore.ipynb
├── scripts/
│   ├── fusao_mercados_fev.py
│   └── processamento_dados.py
├── requirements.txt
└── README.md
```

## Descrição dos Diretórios

- **data_raw/**: Contém os dados brutos das empresas em JSON e CSV.
- **data_processed/**: Armazena os dados processados e combinados.
- **notebooks/**: Notebooks Jupyter para exploração e análise dos dados.
- **scripts/**: Scripts Python para processamento, transformação e fusão dos dados.

## Como Executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

2. Execute o script de fusão dos dados:
   ```sh
   python scripts/fusao_mercados_fev.py
   ```

3. O arquivo consolidado será salvo em `data_processed/dados_combinados.csv`.

## Funcionalidades

- Leitura de dados em JSON e CSV.
- Padronização dos nomes das colunas.
- Fusão dos dados de diferentes fontes.
- Exportação dos dados combinados para CSV.
- Análise exploratória via Jupyter Notebook.

## Requisitos

- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

## Observações

- Certifique-se de que os arquivos de dados estejam nos diretórios corretos antes de executar os scripts.
- O notebook `notebooks/explore.ipynb` pode ser utilizado para análises adicionais e validação dos dados processados.

---

Projeto desenvolvido para fins educativos.