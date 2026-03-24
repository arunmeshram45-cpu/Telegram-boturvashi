from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8373922381:AAGu9lq2SoGArQjLvDz3To3aCu7KRqFBFtg"

keywords = [
"pass",
"open pass",
"panel pass",
"jopi pass",
"blastttt",
"blast",
"open blast",
"jodi blast",
"congratulation",
"congratulations",
"💥",
"✅",
"🤑",
"☺",
"😊",
"🥳",
"❤‍🔥",
"🎉"
]

async def detect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for word in keywords:
        if word in text:

            await update.message.reply_text("""𝐁𝐈𝐆𝐆𝐄𝐒𝐓
𝐂𝐎𝐍𝐆𝐑𝐀𝐓𝐔𝐋𝐀𝐓𝐈𝐎𝐍𝐒 𝐁𝐑𝐎 👑

🏌️ 𝐒𝐔𝐏𝐄𝐑-𝐒𝐇𝐎𝐓 👌👌

🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥

🦁 #MVB 𝐅𝐀𝐌𝐈𝐋𝐘 🦁""")

            break


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), detect))

print("Bot Running...")

app.run_polling()
