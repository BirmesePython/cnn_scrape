This code MUST be ran in a *nix environment, due to a module (dryscrape) not being supported on Windows.
Also, this is tested on and performs correctly on Python 2.7.

To install Beautiful Soup 4:
	1. sudo apt-get update
	2. sudo pip install bs4

To install dryscrape:
	1. sudo apt-get update
	2. sudo apt-get install qt5-default libqt5webkit5-dev build-essential python-lxml python-pip xvfb
	3. sudo pip install dryscrape
	
To run (from the same directory):
	python cnn_scrape.py
	

The code, and screenshots of this code's execution are located in this folder.