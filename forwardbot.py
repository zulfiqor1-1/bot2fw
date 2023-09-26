from pyrogram import Client, filters
from pyrogram.types import Message

# Pyrogramni o'rnating
api_id = "4616406"
api_hash = "e90aba56200d324d8251cc7d909dc623"
bot_token = "6615247386:AAFxjZXJWuW61b2P_FItaU44bRyryonj0QA"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Yozilgan xabarlarda oktyabr, noyabr yoki dekabr so'zi bo'lsa boshqa guruhga yuborish
@app.on_message(filters.text & (filters.regex(r'\boktyabr\b|\bnoyabr\b|\bdekabr\b')))
async def forward_messages_to_another_group(client, message: Message):
    try:
        # Manzil guruhni o'zgartiring
        destination_chat_id = -1001588511301  # Boshqa guruhni identifikatori
        await message.forward(destination_chat_id)
    except Exception as e:
        print(f"Xatolik: {e}")

if __name__ == "__main__":
    app.run()
    