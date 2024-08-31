import requests
from bs4 import BeautifulSoup
import chardet

# URL do site que queremos acessar
url = 'https://www.skoob.com.br/cortesia/finalizando'

# Cabeçalhos para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# Fazer uma requisição GET para obter o conteúdo da página, agora com cabeçalho
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida (status code 200)
if response.status_code == 200:
    # Detectar a codificação correta do conteúdo
    result = chardet.detect(response.content)
    encoding = result['encoding']

    # Decodificar o conteúdo usando a codificação detectada
    content = response.content.decode(encoding, errors='replace')
    
    # Parsear o conteúdo HTML decodificado
    soup = BeautifulSoup(content, 'html.parser')

    # Encontrar todos os elementos <div> com a classe "col-md-3"
    div_elements = soup.find_all('div', class_='col-md-3')
    
    # Lista para armazenar os títulos dos livros
    book_titles = []

    # Iterar sobre os elementos encontrados e extrair os títulos
    for element in div_elements:
        # Encontrar o elemento <div> que contém a classe "title"
        title_div = element.find('div', class_='title')
        if title_div:
            # Encontrar o link dentro da <div class="title"> que contém o título do livro
            title_link = title_div.find('a')
            if title_link:
                # Extrair o texto do link e adicionar à lista de títulos
                book_titles.append(title_link.text.strip())

    # Exibir a lista de títulos dos livros
    for title in book_titles:
        print(title)

else:
    print(f"Falha ao acessar a página. Status code: {response.status_code}")

print("")
input("Pressione Enter para sair...")