import pyrogram
from utils.files import download_file, get_urls

@pyrogram.Client.on_message(pyrogram.filters.command(["download"]))
async def download_handler(bot: pyrogram.Client, update):
    url = update.text[
        update.entities[0].length + 1 :
    ]
    
    input_list = url.split(' ')
    
    if not url:
        await update.reply('**Informe a URL para iniciar o download**')
        return
        
    if ' ' in url:
     
      url = input_list[0]
      url = f'{url}/' if url[len(url)-1:] != '/' else url
      
    urls = await get_urls(url)

    if len(urls) != 0:
        
        await update.reply_text('**Começando o download dos arquivos**',parse_mode='markdown')
        
        episode = input_list[1]
    
        if episode and episode.isdigit():

            urls = urls[int(episode) - 1:]
    
        await download_file(urls, update.chat.id, bot)

    else:
        await update.reply_text('**Erro ao pegar urls**',parse_mode='markdown')
