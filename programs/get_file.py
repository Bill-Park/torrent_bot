from telegram.ext import Updater, MessageHandler, Filters
import os
from bill import login_data

dir_now = os.path.dirname(os.path.abspath(__file__))
dir_home = os.path.join(dir_now, '..')
dir_torrent = os.path.join(dir_home, 'torrent_wait')

print('get file start')
print('dir is : ' + dir_now)

def get_file(bot, update) :
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_torrent, update.message.document.file_name)
    bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('file saved')
    print(update.message.document.file_name)


updater = Updater(login_data.token)

file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()

