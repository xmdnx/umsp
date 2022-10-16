# НУЖНО ЗАПУСТИТЬ ЭТОТ ФАЙЛ

from tkinter import filedialog
import eyed3
from os import listdir
import os
from os.path import isfile, join

debug_mode = True

def dbg(text):
	if debug_mode:
		print('debug: ' + str(text))

file_paths = []

folder_selected = filedialog.askdirectory()
dbg(folder_selected)

onlyfiles = [f for f in listdir(folder_selected) if isfile(join(folder_selected, f))]

i = 0

while i < len(onlyfiles):
	dbg(i)
	if onlyfiles[i].lower().endswith(".mp3"):
		file_paths.append(folder_selected + "/" + onlyfiles[i])
	i += 1

# tag = eyed3.load(file_paths[i])
# tag.tag.title
#         artist
#         album
# tag.info.time_secs

#
# SQLITE3 PART
#

dbg('sql part')

import sqlite3
dbg('import sqlite3 success')

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
dbg('created connection and cursor')

cur.execute("""CREATE TABLE IF NOT EXISTS homepage_track (
    id       INTEGER       NOT NULL
                           PRIMARY KEY AUTOINCREMENT,
    title    VARCHAR (100) NOT NULL,
    author   VARCHAR (100) NOT NULL,
    duration VARCHAR (10)  NOT NULL,
    file     TEXT          NOT NULL
);""")
conn.commit()
dbg('executed create table, and commited')

dbg('cycle starts')
for i in range(len(file_paths)):
	tag = eyed3.load(file_paths[i])
	dbg('tag inited')

	cur.execute("INSERT OR REPLACE INTO 'homepage_track' VALUES(?, ?, ?, ?, ?)", (str(i), tag.tag.title, tag.tag.artist, str(round(tag.info.time_secs)), file_paths[i]))
	dbg('executed command')

	conn.commit()
	dbg('commited')

dbg('cycle success!')

conn.close()
dbg('connection closed!')

dbg('runserver...')
os.system('python manage.py runserver')