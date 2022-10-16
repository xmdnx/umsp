from tkinter import filedialog
import eyed3
from os import listdir
from os.path import isfile, join

debug_mode = False

def dbg(text):
	if debug_mode:
		print('debug: ' + text)

file_paths = []

folder_selected = filedialog.askdirectory()
dbg(folder_selected)

onlyfiles = [f for f in listdir(folder_selected) if isfile(join(folder_selected, f))]

dbg(onlyfiles)

i = 0

while i < len(onlyfiles):
	dbg(i)
	if onlyfiles[i].lower().endswith(".mp3"):
		file_paths.append(folder_selected + "/" + onlyfiles[i])
	i += 1

for i in range(len(file_paths)):
	dbg(file_paths[i])
	i += 1

from rich.console import Console
from rich.table import Table

table = Table(title="Все песни из папки " + folder_selected)

table.add_column("Название", style="cyan", no_wrap=True)
table.add_column("Исполнитель", style="magenta")
table.add_column("Альбом", style="green")

for i in range(len(file_paths)):
	tag = eyed3.load(file_paths[i])
	table.add_row(tag.tag.title, tag.tag.artist, tag.tag.album)

console = Console()
console.print(table)