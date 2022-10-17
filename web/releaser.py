import os, shutil
import pathlib

if os.path.exists("db.sqlite3"):
	os.remove("db.sqlite3")
else:
	print("The file does not exist")

if os.path.exists('homepage/migrations'):
	shutil.rmtree(str(pathlib.Path(__file__).parent.resolve()) + '/homepage/migrations')
f = open('db.sqlite3', 'w')
f.close()