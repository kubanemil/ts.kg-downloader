from time import *
from os import startfile

while True:
	now = localtime(time())
	if now.tm_hour >= 6 and now.tm_hour <= 13:
		startfile(r'.\scan_for_new_episodes.pyw')
		sleep(8*60*60)
