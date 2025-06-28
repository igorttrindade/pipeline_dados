import json
import csv

class Dados:
    def __init__(self):
        self.dados = self.leitura_dados()
        self.nome_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    def __leitura_json(self):
        dados_json = []
        with open(self.__path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def __leitura_csv(self):
        dados_csv = []
        with open(self.__path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for linha in spamreader:
                dados_csv.append(linha)
        return dados_csv
    
    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []
        if tipo_dados == 'csv':
            return cls.__leitura_csv(path)
        elif tipo_dados == 'json':
            return cls.__leitura_json(path)
        return dados

    def __get_columns(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key,value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nome_colunas = self.__get_columns()

    def __size_data(self):
        return len(self.dados)
    
    def join_data(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list, 'list')
    
    def __transforma_data_table(self):
        dados_combinados_tabela = [self.nome_colunas]
        for linha in self.dados:
            row = []
            for coluna in self.nome_colunas:
                row.append(linha.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(row)
        return dados_combinados_tabela
    
    def save_data(self, path):
        dados_combinados_tabela = self.__transforma_data_table()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)