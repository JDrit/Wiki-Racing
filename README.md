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
	Uses the bottle python web server framework to handle requests. The main path is
	/path but everything gets redirected to /path as well. The server handles 404 and
	500 errors. It uses a templates system to help display the path to the user. It imports
	the methods from pathFinder.py.