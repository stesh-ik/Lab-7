import json, requests

def weather():
    key = 'abc05a572e4b13232e369b5e72f6ca96'
    name = 'London'
    response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid={key}')
    result = json.loads(response.text)
    temperature = round(result['main']['temp']-273, 1)
    humidity = result['main']['humidity']
    pressure = result['main']['pressure']
    print(f"Город: {name} \nТемпература: {temperature}\nВлажность: {humidity}\nДавление: {pressure}")


def newsapi():
    url = ('https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=350b881e02674c69b75bf2a2244818ba')
    response = requests.get(url)
    result = json.loads(response.text)
    print("3 главные статьи из BBC-News:")
    for i, data in enumerate(result['articles'], start=1):
        if i == 4: break
        title = data['title']
        publisher = data['author']
        description = data['description']
        print(f'{i}. {title} \nИздатель: {publisher} \nОписание: {description}')

weather()
print()
newsapi()