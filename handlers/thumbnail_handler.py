from pyrogram import Client, filters
from PIL import Image
import os

@Client.on_message(filters.photo)
async def save_thumbnail(bot: Client, update):
 
  try:
    await bot.download_media(
      update,
      file_name = f'thumbnails/{update.chat.id}/thumbnail.jpg'
    )
    image = Image.open(f'thumbnails/{update.chat.id}/thumbnail.jpg')
    
    new_image = image.resize((320,320))
    new_image.save(f'thumbnails/{update.chat.id}/thumb.jpg')

    image.close()

    await update.reply_text('**Thumbnail salva**', parse_mode='markdown')
  
  except:
    await update.reply_text('**Erro ao salvar a thumbail**', parse_mode='markdown')

@Client.on_message(filters.command(['del']))
async def delete_thumbnail(bot: Client, update):
  
  try:
    
    os.remove(f'thumbnails/{update.chat.id}/thumb.jpg')
    os.remove(f'thumbnails/{update.chat.id}/thumbnail.jpg')
    await update.reply_text('**Thumbnail deletada**', parse_mode='markdown')

  except:

    await update.reply_text('**Erro ao deletar a thumbail**',parse_mode='markdown')

@Client.on_message(filters.command(['thumbnail']))
async def send_thumbnail(bot: Client, update):

  IMAGE = os.path.exists(f'thumbnails/{update.chat.id}/thumbnail.jpg')

  if IMAGE:
    await bot.send_photo(
      update.chat.id,
      f'thumbnails/{update.chat.id}/thumbnail.jpg'
    )

  else:
    
    await update.reply_text(
      "Não há nenhuma thumbnail"
    )