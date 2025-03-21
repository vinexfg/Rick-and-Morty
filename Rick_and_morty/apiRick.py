import requests
import webbrowser


def personagem_digitado():
        print('Digite o nome do personagem...')
        personagem = input('Nome: ')
        return personagem

    
def consulta_nome(personagem):
    url = f'https://rickandmortyapi.com/api/character/?name={personagem}'
    resultado = requests.get(url)

    if resultado.status_code == 200:
          dados = resultado.json()
          
          if dados['results']:
               personagem = dados['results'][0]
               return personagem
          else:
                print('Nenhum personagem encontrado.')
                return None
    else:
          print('Erro na API.')

def obter_episodios(episodios_urls):
     episodios = []
     for url in episodios_urls:
          resposta = requests.get(url)
          if resposta.status_code == 200:
               dados = resposta.json()
               episodios.append(dados['name'])
          else:          
               episodios.append('Episodio Desconhecido')
     print(episodios)
     return episodios
     
        
def gerar_html(personagem):
     if personagem:
        episodios = obter_episodios(personagem['episode'])
        episodios_lista = "".join(f"<li>{ep}</li>" for ep in episodios)
     return f"""
        <!DOCTYPE html>
        <html lang="pt">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{personagem['name']}</title>
        </head>
        <body>

        <h1>{personagem['name']}</h1>
        <img src="{personagem['image']}" alt="{personagem['name']}">
        <h3>DADOS:</h3>

        <p><strong>Nome:</strong> {personagem['name']}</p>
        <p><strong>Status:</strong> {personagem['status']}</p>
        <p><strong>Espécie:</strong> {personagem['species']}</p>
        <p><strong>Gênero:</strong> {personagem['gender']}</p>

        <h3>Episodios em que apareceu:<h3>
        </ul>
               {episodios_lista}
        </ul>


        </body>
        </html>
        """
     

personagem = personagem_digitado()
personagem_achado = consulta_nome(personagem)
html_inserido = gerar_html(personagem_achado)


with open('indexas.html', 'w', encoding='utf-8')as arquivo:
     arquivo.write(html_inserido)

webbrowser.open('indexas.html')

