import telebot

TOKEN = "8495793480:AAHbDw_ignazY_2H2jLoKj2B-eaBvToxs6M"

bot = telebot.TeleBot(TOKEN)

HTML_TAGS = """
HTML tags:
<html>
<head>
<title>
<body>
<h1> - <h6>
<p>
<a>
<img>
<ul>
<ol>
<li>
<div>
<span>
<form>
<input>
<button>
<table>
<tr>
<td>
<th>
<br>
<hr>
"""

CSS_TAGS = """
CSS properties:
color
background
background-color
width
height
margin
padding
border
border-radius
display
flex
grid
justify-content
align-items
position
top
left
right
bottom
font-size
font-family
font-weight
text-align
box-shadow
opacity
"""

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom 👋\n\n"
        "👉 html deb yoz — HTML taglar chiqadi\n"
        "👉 css deb yoz — CSS propertylar chiqadi"
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    text = message.text.lower()

    if text == "html":
        bot.send_message(message.chat.id, HTML_TAGS)
    elif text == "css":
        bot.send_message(message.chat.id, CSS_TAGS)
    else:
        bot.send_message(
            message.chat.id,
            "❌ Noto‘g‘ri buyruq\n\n"
            "html yoki css deb yoz"
        )

print("Bot ishga tushdi! Telegramda /start ni bosing...")  # terminalga chiqadi

try:
    bot.polling(none_stop=True)  # Windows va Mac-da doimiy ishlash
except Exception as e:
    print("Botda xatolik:", e)