import asyncio
import aiohttp
from bs4 import BeautifulSoup

TOKEN = None


def set_token(token):
    global TOKEN
    TOKEN = token


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_page_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.text


async def send_message(chat_id, text):
    async with aiohttp.ClientSession() as session:
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {
            'chat_id': chat_id,
            'text': text
        }
        async with session.post(url, data=payload) as response:
            return await response.json()


async def handle_message(message):
    chat_id = message['chat']['id']
    text = message['text']

    if text.startswith('/get_title '):
        url = text.split('/get_title ')[1]
        title = await get_page_title(url)
        await send_message(chat_id, title)
    else:
        await send_message(chat_id, 'Unknown command.')


async def main():
    async with aiohttp.ClientSession() as session:
        url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
        async with session.get(url) as response:
            updates = await response.json()

            if 'result' in updates:
                for update in updates['result']:
                    if 'message' in update:
                        message = update['message']
                        await handle_message(message)


if __name__ == '__main__':
    asyncio.run(main())