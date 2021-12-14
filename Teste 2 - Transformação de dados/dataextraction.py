from tabula import read_pdf
import csv
from pathlib import Path
import os, glob
from zipfile import ZipFile
from os.path import basename

def main():
    path = os.getcwd()
    prev_path = os.path.abspath(os.path.join(path, os.pardir))
    file_name = 'padrao-tiss_componente-organizacional_202111.pdf'
    file_path = os.path.join(prev_path, 'Teste 1 - Web Scraping', file_name)
    tables = read_pdf(file_path, pages = "114-120")
    search_tables = ['Tabela de Tipo do Demandante', 'Tabela de Categoria do Padrão TISS', 'Tabela de Tipo de Solicitação']

    # quadro 30 (página 114) - Tabela de Tipo Demandante
    # quadro 31 (página 115) - Tabela de Categoria do Padrão TISS
    # quadro 32 (página 120) - Tabela de tipo de solicitação

    # busca as tabelas da página 114 até a 120 e as escreve em csvs
    number_of_table = -1
    if (len(tables)):
        for table in tables:
            if('Tabela' in table.iloc[0].to_string()):
                number_of_table += 1
                table.dropna(inplace = True)
                table.to_csv(search_tables[number_of_table]+'.csv', sep=';', encoding='utf-8', index = False, header = True)
            else:
                table.to_csv(search_tables[number_of_table] + '.csv', mode='a', sep=';', encoding='utf-8', index = False, header=False)

    # cria zip com as tabelas

    csv_files = glob.glob(os.getcwd() + f"/*.csv")  # pega todos os arquivos csv do diretório atual

    if(len(csv_files) > 0):
        zip = ZipFile(f'Teste_joao_pedro_gomes_de_souza.zip', 'w')
        for file in csv_files:
            zip.write(file, basename(file)) #

        zip.close()
            

main()
