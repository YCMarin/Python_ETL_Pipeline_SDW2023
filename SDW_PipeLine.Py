import pandas as pd
import requests 
import json
#import openai

### Extract
df = pd.read_csv("SDW.CSV") #lendo arquivo
dt = pd.read_csv("textos.CSV")

user_ids = df['UserID'].tolist() #transf colunas do arv em lista py
textos = dt["Textos"].tolist()
print(user_ids)
print(textos)

#link da api
sdw2023_api_url = "https://sdw-2023-prd.up.railway.app"

#função para pegar usário da API pelo código
def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

#atribui apenas se for not None
users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

### Transformação
### Uso de openai_API
"""openai_api_key = ''
openai.api_key = openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "Você é um especialista em marketing bancário"
      },
      {
          "role": "user", 
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
      }
    ]
  )
  return competion.choices[0].message.content.strip('\"')
 """

for user in users:
  novidades = textos
  print(novidades)

  for texto in novidades:
    user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/pix.svg",
      "description": texto
    })


def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")
