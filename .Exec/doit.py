import os
from colorama import Fore, Style
from tqdm import tqdm
index_file = ""

import sys,time,random
def progressBar(count_value, total, suffix=''):
    bar_length = 100
    filled_up_Length = int(round(bar_length* count_value / float(total)))
    percentage = round(100.0 * count_value/float(total),1)
    bar = '=' * filled_up_Length + '-' * (bar_length - filled_up_Length)
    sys.stdout.write('[%s] %s%s ...%s\r' %(bar, percentage, '%', suffix))
    sys.stdout.flush()

def menu():
	print(Fore.MAGENTA)
	print("#"*25)
	print("1. Update your Repo")
	print("2. Edit your page")
	print("3. End the loop")
	print(Style.RESET_ALL)

def choice():
	menu()
	try:
		ch = int(input(Fore.GREEN+"Enter your choice:\t"+Fore.YELLOW))
		return ch
	except Exception as e:
		print("Error occurred",e)
		choice()

def action(ch):
	if ch == 1:
		message = input("Enter your commit message:\t")
		c1 = "git add ."
		c2 = "git commit -m "+message
		c3 = 'git push -u origin main'
		os.system(c1)
		os.system(c2)
		os.system(c3)
		rand_number = random.randint(80,120)

		barcolors =['ffa500','0000FF','#008080','#6E260E','#C04000','#008000','#FF5F1F','#FF00FF','#E30B5C',]
		c= random.choice(barcolors).lower()
		print(Fore.WHITE+"Processing the deployment")
		time.sleep(0.24)
#		print("Please wait for ",rand_number,"seconds")
#		time.sleep(rand_number)
		denominator = random.randint(40,70)
		for i in tqdm(range(0, 100), colour=c, desc ="Progress: "):
			time.sleep(rand_number/denominator)
		print(Fore.GREEN+"All done. Go to your website to verify changes.")
	if ch == 2:
		c = "nano /home/kali/MyProjects/Mywebsite/codeaalok.github.io/index.html"
		os.system(c)
	if ch == 3:
		print("Exiting now")
		sys.exit()


while True:
	ch = choice()
	action(ch)
