import requests

word = input("Enter a word: ")

api_url = 'https://api.api-ninjas.com/v1/dictionary?word={}'.format(word)
response = requests.get(api_url, headers={'X-Api-Key': 'tsmXHKRiy5PHVGAulzn3XQ==W3c6TikLVtPWoiYI'})
data = response.json()

if response.status_code == requests.codes.ok:
    print(data['definition'])
else:
    print("Error:", response.status_code, response.text)
