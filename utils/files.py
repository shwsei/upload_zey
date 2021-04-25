import aiohttp, asyncio, json, os, requests
from humanfriendly import format_size
from pyrogram import Client


async def get_urls(url: str) -> list:
  
  async with aiohttp.ClientSession() as session:
    RESPONSE = await session.post(
      url,
      data={
        'page_index': 0
      }
    )

    try:

      JSON = json.loads(
        await RESPONSE.text()
      )
  
      LINKS = [ {
          'url': f"{url}{link['name']}",
          'name': link['name']
        } for link in JSON['data']['files']
      ]

      return LINKS

    except:
      return []


async def download_file(data: list, chat_id: int, bot: Client):

  if len(data) != 0:

    EPISODE = data.pop(0)

    EDIT = await bot.send_message(
      chat_id, f'**Começando o download do arquivo**\n`{EPISODE["name"]}`',
      parse_mode="markdown"
    )

    request = requests.get(EPISODE['url'], stream = True)
    if request.status_code == 200:
    
        with open(f'temp/{EPISODE["name"]}', 'wb') as file:
            for chunk in request.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

    else:
      await bot.edit_message_text(
        chat_id, EDIT.message_id, 
        '**Erro ao fazer o download do arquivo!**',
        parse_mode="markdown"
      )
      
      return None

    SIZE = format_size(os.path.getsize(f'temp/{EPISODE["name"]}'))
    
    await bot.edit_message_text(
      chat_id,
      EDIT.message_id,
      f'**Começando o upload do arquivo**`\n{EPISODE["name"]}`\nTamanho: `{SIZE}`',
      parse_mode="markdown"
    )

    await upload(chat_id, bot, EPISODE['name'])

    await bot.delete_messages(chat_id, EDIT.message_id)

    await bot.send_message(
      chat_id,
      f'**Upload finalizado**\n`{EPISODE["name"]}`\nTamanho: `{SIZE}`', 
      parse_mode='markdown'
    )
    os.remove(f'temp/{EPISODE["name"]}')

    await download_file(data, chat_id, bot)

  else:
  
    await bot.send_message(chat_id, '**Download e upload dos arquivos finalizado**', parse_mode='markdown')


async def upload(chat_id: int, bot: Client, filename: str):
  
  if not os.path.exists(f'thumbnails/{chat_id}/thumb.jpg'):

    await bot.send_document(
      chat_id=chat_id,
      document=f'temp/{filename}',
      caption=filename
    )
  
  else:

    await bot.send_document(
      chat_id=chat_id,
      document=f'temp/{filename}',
      caption=filename,
      thumb=f'thumbnails/{chat_id}/thumb.jpg'
    )
