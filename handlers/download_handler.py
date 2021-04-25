import pyrogram
from utils.files import download_file, get_urls

@pyrogram.Client.on_message(pyrogram.filters.command(["download"]))
async def download_handler(bot: pyrogram.Client, update):
    url = update.text[
        update.entities[0].length + 1 :
    ]

    if not url:
        await update.reply('**Informe a URL para iniciar o download**')
        return
        
    if url[len(url)-1:] != '/':
        url = f'{url}/'

    urls = await get_urls(url)

    if len(urls) != 0:
        await update.reply_text('**Começando o download dos arquivos**',parse_mode='markdown')
        await download_file(urls, update.chat.id, bot)

    else:
        update.reply_text('**Erro ao pegar urls**',parse_mode='markdown')
