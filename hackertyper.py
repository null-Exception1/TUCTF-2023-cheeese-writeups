import requests

cookies = {
    'uuid': '4f8ab00a-83fe-40ff-a648-122db0a44af1',
}

headers = {
    'authority': 'hacker-typer.tuctf.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://ctfd.tuctf.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

from bs4 import BeautifulSoup
response = requests.get('https://hacker-typer.tuctf.com/', cookies=cookies, headers=headers)
html = BeautifulSoup(response.text,features="html.parser")
data = {
        'word': html.find('strong',{'name':'word-title'}).text,
    }

# entire thing is just a ping pong game, just keep echoing the words to the site, with your uuid cookies

while True:
    response = requests.post('https://hacker-typer.tuctf.com/check_word', cookies=cookies, headers=headers, data=data)

    print("[RESP] ",response.text) # the response containing the next word

    data = {
        'word': eval(response.text)['next_word'],
    }

    print("[SEND] ",data) # sending the next word back