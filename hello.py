import asyncio
from pyrogram import Client

api_id = 22931292
api_hash = "8a50db8b70f8cbcbc013f013b6a58ac7"


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())
