Wiki-Racing
===========
This project's goal is to be able to find the best path between any two 
wikipedia articles. 

Files:
- parser.py
	Reads the .xml file from wikipedia and pulls out the article title and all
	the links in it. It saves each (title, link) pair as a dictionary using
	cPickle.

- pathFinder.py
	Loads the data using cPickle into a dictionary of Node class. It then runs
	the aStar algorithm over the dictionary to find the best path between the
	two articles.
	
	Node class:
	- title
	- links
	- parent
	- distance

- server.py (TBD)
	Will use bottle.py to host a small webserver to run the pathfinder through
	a website.