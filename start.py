import ts_kg
from win32com.shell import shell, shellcon
import shutil
import win32com.client
import pythoncom
import os

ts_kg.add_show()
print('Wait while adding to list...')
for show in ts_kg.shows_link_list():
    ts_kg.add_to_watched(show)
os.startfile(r'.\sheduler.pyw')


def get_startup_directory(common):   
    return shell.SHGetFolderPath(0, (shellcon.CSIDL_STARTUP, shellcon.CSIDL_COMMON_STARTUP)[common], None, 0)
startup_dir = get_startup_directory(0)
dest =  startup_dir+'\\sheduler.pyw'

path = os.path.join(startup_dir, 'sheduler.lnk')
target = r'.\sheduler.pyw'

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WindowStyle = 7 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()

