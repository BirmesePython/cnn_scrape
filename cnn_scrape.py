print "Beginning Scrape... Takes ~20s" #CSCE 4444, Justin Muskopf, jfm0103 - HW 1
from bs4 import BeautifulSoup; import dryscrape; dryscrape.start_xvfb() #Import libraries and Start X-Server
session = dryscrape.Session(); session.visit("http://www.cnn.com") 	#Create session and go to cnn.com
page = BeautifulSoup(session.body(), 'lxml'); 				#Parse body of page
for category in ['Health', 'Tech', 'Travel']: 				#Loop through each category, then find and print headlines
	print "--------------" + category + "--------------";
	Find = page.find('h2', text = category).parent.parent.find_all('div', {'class': 'strip-rec-link-title ob-tcolor'}) + page.find('h2', text = category).parent.parent.find_all('span', {'class': 'cd__headline-text'})
	for obj in set(Find): print obj.text
