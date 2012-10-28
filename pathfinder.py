import time
import datetime
import cPickle as pickle

class Node:
   
    def __init__(self, title, links):
        self.title = title        # the title of the article
        self.links = links        # the titles of all the articles linked to
        self.parent = ''          # the parent article title for path finding
        self.distance = 1000000   # the number of articles it takes to get to


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
    start = dic[start]
    end = dic[end]
    
    openList.add(start)
    while openList:
        start = sorted(openList, key=lambda inst: inst.distance)[0]
        openList.remove(start)
        closedList.add(start)
        
        for article in start.links.split(':'):
            if article in dic: # if the article is an actual link
                if dic[article] not in closedList:
                    dic[article].distance = start.distance + 1
                    openList.add(dic[article])
                    dic[article].parent = start.title
                if dic[article].distance > start.distance + 1: # sets the parent to another path if it is shorter
                    dic[article].distance = start.distance + 1
                    dic[article].parent = start.title
                if article == end.title:
                    return True
    return False
          
def pathMaker(dic, start, end):
    '''
    Makes the list of articles to go to to get from the start to the finish
    dic (dictionary): the dictionary of the articles
    start (String): the start article's name
    end (String): the end article's name
    Returns a list of the articles to go to
    '''
    path = []
    while not dic[end].parent == '':
        path.append(end)
        end = dic[end].parent
    path.append(start)
    path.reverse()
    return path

def main():
    start = 'Anarchism'
    end = 'Ordinary (officer)'
    print('path finder start')
    dic = makeDic('output.txt')
    dic[start].distance = 0
    startTime = time.clock()
    print(aStar(dic, start, end))
    endTime = time.clock()
    print('Time to find path: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    print('-----------------------------------------')
    print(pathMaker(dic, start, end))

#main()
