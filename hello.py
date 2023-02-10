from pyrogram import Client

api_id = 22931292
api_hash = "8a50db8b70f8cbcbc013f013b6a58ac7"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

app.run()
