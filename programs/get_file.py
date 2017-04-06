from telegram.ext import Updater, MessageHandler, Filters
import os
from bill import login_data
import transmissionrpc

dir_now = os.path.dirname(os.path.abspath(__file__))
dir_home = os.path.join(dir_now, '..')
dir_torrent = os.path.join(dir_home, '..', 'usb1', 'progress')

print('get file start')
print('dir is : ' + dir_now)

torrent_client = transmissionrpc.Client('localhost', port=9091, user=login_data.user, password=login_data.passwd)

def add_file(torrent_file_path) :
    for torrent_file in os.listdir(torrent_file_path) :
        torrent_path = os.path.join(dir_torrent, torrent_file)
        torrent_client.add_torrent(torrent_path)

def get_file(bot, update) :
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_torrent, update.message.document.file_name)
    print(file_url)
    bot.getFile(file_id_short).download(file_url)
    print('got')
    update.message.reply_text('file saved')
    torrent_client.add_torrent(file_url)
    print(t_client.get_torrents())


updater = Updater(login_data.token)
print(login_data.token)
file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()

