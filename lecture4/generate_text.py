import urllib
import os

'''this code produces a large directory with files containing random text'''

k=0
for i in range(1,21):
	k+=1

	directory = "fortune" + str(i)
	os.mkdir(directory)
	os.chdir(directory) 

	file_ob = open("fortune"+str(k)+".txt", "w")
	resp = urllib.urlopen("http://www.iheartquotes.com/api/v1/random")
	web_pg = resp.read()
 	file_ob.write(web_pg)
	file_ob.close()

	file_ob = open("fortune"+str(k)+".log", "w")
	resp = urllib.urlopen("http://www.iheartquotes.com/api/v1/random")
	web_pg = resp.read()
	file_ob.write(web_pg)
	file_ob.close()