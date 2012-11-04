Wiki-Racing
===========
This project's goal is to be able to find the best path between any two 
wikipedia articles. 

Files:
- parser.py
	Reads the .xml file from wikipedia and pulls out the article title and all
	the links in it. It saves each (title, link) pair as a list using
	cPickle.

- pathFinder.py
	Holds the methods used by the server to load the articles into memory and find
	the best path between any two articles. The data for each class is stored in
	a python dictionary with the key being the article name and the value being a
	string of all the links that the article has. The pathfinder method has instance
	list for distances and parents of each article so that mult. connections
	do not interfer with each other.	

- server.py
	Uses the bottle python web server framework to handle requests. The main path is
	'/path' but everything gets redirected to /path as well. The server handles 404 and
	500 errors. It uses a templates system to help display the path to the user. It imports
	the methods from pathFinder.py.

- pathViewer.tpl
	The template file used for the bottle server. It displays the result from the give input
	in a list.

- index.tpl
	The template for the start page as long as the error message page.