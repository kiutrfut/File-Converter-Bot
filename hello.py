from pyrogram import Client

api_id = 22931292
api_hash = "8a50db8b70f8cbcbc013f013b6a58ac7"
bot_token = "5562112612:AAH7Sbz2iIAdoPknjv0FnuiNbiDa_5OFYQA"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

app.run()
