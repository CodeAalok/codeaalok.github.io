import os

message = input("commit message:\t")
c1 = "git add ."
c2 = 'git commit -m  "'+ message+'"'
c3  = 'git push -u origin main'
#print(c2)

def o(c):
	print(c)
	os.system(c)

o(c1)
o(c2)
o(c3)
