from pyrogram import Client, filters

START_TEXT = """
Olá, sou um bot que irá fazer o download dos animes do site: `https://5.orezraey.workers.dev/0:/`
Use o comando /help para verificar minhas funcionalidades
"""

HELP_TEXT = """
`Fazendo o download`
Use o comando `/download` para iniciar o download dos arquivos

Ex: `/download https://5.orezraey.workers.dev/0:/Animes/Bleach/M%C3%BAltiplas%20Legendas%2FDual%20%C3%81udio%20-%20BD%201080p%20x265/`

`Thumbnails customizadas`

-> **Envie uma imagem que deseja usar como thumbnails nos arquivos, 
após será todos os arquivos baixados serão enviados com esta thumbnail
Você pode utilizar o comando** `/del` **para deletar a thumbnail e o
comando /thumbnail para visualizar a thumbnail atual**
"""


@Client.on_message(filters.command(['start']))
async def start(bot: Client, update):
  await update.reply_text(
    START_TEXT,
    parse_mode='markdown'
  ) 


@Client.on_message(filters.command(['help']))
async def help(bot: Client, update):
  await update.reply_text(
    HELP_TEXT,
    parse_mode='markdown'
  )

@Client.on_message(filters.command(['source']))
async def help(bot: Client, update):
  await bot.send_message(
    update.chat.id, "Source: https://github.com/Lewizh11/upload_zey\nBy: @ShuseiKagari", 
  )