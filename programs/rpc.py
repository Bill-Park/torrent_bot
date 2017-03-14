import transmissionrpc
import os
from telegram.ext import Updater, MessageHandler, Filters
from bill import login_data

dir_now = os.path.dirname(os.path.abspath(__file__))
dir_home = os.path.join(dir_now, '..')

print('home : ' + dir_now)

t_client = transmissionrpc.Client('localhost', port=9091, user=login_data.user, password=login_data.passwd)



'''
t_main = t_client.get_torrent(0)
t_main.start()

print(tc.get_torrents)

t_main.stop()
'''
