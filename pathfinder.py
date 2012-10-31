import time
import datetime
import cPickle as pickle

class Node:
   
    def __init__(self, title, links):
        self.title = title        # the title of the article
        self.links = links        # the titles of all the articles linked to

def makeDic(fname):
    '''
    Reads in from the file specified, which each line is a list with 2 indexes,
        title and links
    fname (String): the file name to pickle from
    Returns a dictionary with the article titles as the keys and Node classes
        as the value
    '''
    wikiInput = open(fname)
    dic = {}
    count = 0
    startTime = time.clock()
    while True:
        try:
            element = pickle.load(wikiInput) # single article, [0] is title, [1] is links
            dic[element[0]] = Node(element[0], element[1])
            count += 1
            if count % 1000000 == 0:
                print('loaded ' + format(count, ',d') + ' elements')
        except EOFError:
            break # breaks when all articles have been read
    endTime = time.clock()
    print('Time to load dictionary: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    wikiInput.close()
    return dic

def aStar(dic, start, end):
    '''
    Runs the A Star Algorithm on the passed dictionary
    dic (dictionary): the dictionary containing the classes representing the articles
    start (Node): the node to start at
    end (Node): the node to end at
    Returns True if path found, False if no path was found
    '''
    openList = set()   # the articles that can be got to, but have not be look at
    closedList = set() # the articles that have already be processed
    distances = {}     # holds the distances for each article from the start
    parents = {}       # holds the parent article for the best path for the articles

    start = dic[start]
    end = dic[end]
    distances[start.title] = 0
    openList.add(start)
    
    while openList:
        #start = sorted(openList, key=lambda inst: inst.distance)[0]
        start = sorted(openList, key=lambda inst: distances[inst.title])[0]
        openList.remove(start)
        closedList.add(start)
        
        for article in start.links.split(':'):
            if article in dic: # if the article is an actual link
                if dic[article] not in closedList:
                    distances[article] = distances[start.title] + 1
                    ###dic[article].distance = start.distance + 1
                    openList.add(dic[article])
                    parents[article] = start.title
                    ###dic[article].parent = start.title
                if distances[article] > distances[start.title] + 1:
                    distances[article] = distances[start.title] + 1
                    parents[article] = start.title
                if article == end.title:
                    return parents
    return False
          
def pathMaker(parents, start, end):
    '''
    Makes the list of articles to go to to get from the start to the finish
    dic (dictionary): the dictionary of the articles
    start (String): the start article's name
    end (String): the end article's name
    Returns a list of the articles to go to
    '''
    path = []
    while not end == start:
        path.append(end)
        end = parents[end]
    path.append(start)
    path.reverse()
    return path

def main():
    start = 'Vladimir Putin'
    end = 'Ubisoft'
    dic = makeDic('output.txt')
    dic[start].distance = 0
    startTime = time.clock()
    parents = aStar(dic, start, end)
    endTime = time.clock()
    print('Time to find path: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    print('-----------------------------------------')
    print(pathMaker(parents, start, end))

main()
