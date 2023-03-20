import os
from colorama import Fore, Style
import time
index_file = ""
def menu():
	print(Fore.RED)
	print("#"*25)
	print("1. Update your Repo")
	print("2. Edit your page")
	print(Style.RESET_ALL)
	
def choice():
	menu()
	ch = int(input(Fore.GREEN+"Enter your choice:\t"+Fore.YELLOW))
	return ch
	
def action(ch):
	if ch == 1:
		message = input("Enter your commit message:\t")
		c1 = "git add ."
		c2 = "git commit -m "+message
		c3 = 'git push -u origin main'
		os.system(c1)
		time.sleep(4)
		os.system(c2)
		os.system(c3)
		print("All done. Exiting")
	if ch == 2:
		c = "nano /home/kali/MyProjects/Mywebsite/codeaalok.github.io/index.html"
		os.system(c)


while True:
	ch = choice()
	action(ch)
