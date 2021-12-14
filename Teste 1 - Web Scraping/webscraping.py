from bs4 import BeautifulSoup
import requests


def main():
    url = 'https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss'
    html = requests.get(url).content
    bsObject = BeautifulSoup(html, 'html.parser') #obtendo o html da página

    linksList = bsObject.find_all("a", class_="alert-link", href = True) #recebe todos os links da página
    link_to_pdf = linksList[0]['href'] # pega o link da versão mais recente

    # agora é necessário fazer uma outra request para a página do link acima
    html = requests.get(link_to_pdf).content
    bsObject = BeautifulSoup(html, 'html.parser')
    download = None
    title_latest = 'Componente Organizacional'

    #itera sobre as linhas da tabela onde estão os downloads
    for row in bsObject.find_all('tr')[1:]:
        if (row.text.split('\n')[1] == title_latest): # verifica se na linha o texto equivale ao componente organizacional
            download = row.find_all('a', href = True)[0]['href'] # recebe o link presente na linha
            
    #cria o arquivo e escreve o binário da requisição
    with open(f"{download.split('/')[-1]}", 'wb') as file:
        file.write(requests.get(download).content)

main()