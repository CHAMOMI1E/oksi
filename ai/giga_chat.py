import json
import uuid
import aiohttp
from aiohttp import BasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
SECRET = os.getenv("CLIENT_SECRET")


async def get_access_token() -> str:
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
    }
    payload = {"scope": "GIGACHAT_API_PERS"}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, auth=BasicAuth(CLIENT_ID, SECRET), data=payload,
                                ssl=False) as res:
            res_json = await res.json()
            access_token = res_json["access_token"]
            return access_token


async def get_image(file_id: str, access_token: str):
    url = f"https://gigachat.devices.sberbank.ru/api/v1/files/{file_id}/content"
    headers = {
        'Accept': 'application/jpg',
        'Authorization': f'Bearer {access_token}'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            return await response.read()


async def send_prompt(msg: str, access_token: str):
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "system",
                "content": "Ты виртупльный консултанат 'Окси', ты помогаешь составлять статьи для телеграмм каналов и подсказываешь что тут и как"
                           "Твой создатель: Романейко Илья"},
            {
                "role": "user",
                "content": msg,
            }
        ],
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload, ssl=False) as response:
            res_json = await response.json()
            return res_json["choices"][0]["message"]["content"]


async def sent_prompt_and_get_response(msg: str, access_token: str):
    res = await send_prompt(msg, access_token)
    data, is_image = get_file_id(
        res)  # Предполагаемая функция get_file_id должна быть асинхронной, если это необходимо.
    if is_image:
        data = await get_image(file_id=data, access_token=access_token)
    return data, is_image
