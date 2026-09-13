import httpx

from app.config import settings

TELEGRAM_API = f"https://api.telegram.org/bot{settings.telegram_bot_token}"


async def send_message(chat_id: int, text: str) -> None:
    async with httpx.AsyncClient() as client:
        await client.post(f"{TELEGRAM_API}/sendMessage", json={"chat_id": chat_id, "text": text})


async def get_file_path(file_id: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{TELEGRAM_API}/getFile", params={"file_id": file_id})
        response.raise_for_status()
        return response.json()["result"]["file_path"]


async def download_file(file_path: str) -> bytes:
    file_url = f"https://api.telegram.org/file/bot{settings.telegram_bot_token}/{file_path}"
    async with httpx.AsyncClient() as client:
        response = await client.get(file_url)
        response.raise_for_status()
        return response.content
