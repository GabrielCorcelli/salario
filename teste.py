import requests, random, json
id=str(input('NUMERO: '))
jogador=str(input('JOGADOR: '))
data = {"id": id, "jogador": jogador}
response = requests.post('http://pfsenseassec.netextreme.com.br:3000/game', json=data)
print(response.status_code)
if response.status_code != 201:
    print('GANHOU!!')
else:
   print('TENTA NOVAMENTE')
