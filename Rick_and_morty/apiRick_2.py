import requests

# api_moedas = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
requsicao = requests.get('https://teste-27ea2-default-rtdb.firebaseio.com/.json')

print(requsicao)
print(requsicao.json)
