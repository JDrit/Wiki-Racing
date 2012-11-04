import time
import datetime
import cPickle as pickle

def makeDic(fname):
    '''
    Reads in from the file specified, which each line is a list with 2 indexes,
        title and links
    fname (String): the file name to pickle from
    Returns:
        a dictionary with the article titles as the keys and links in a string
            format as the values
    '''
    wikiInput = open(fname)
    dic = {}
    count = 0
    startTime = time.clock()
    while True:
        try:
            element = pickle.load(wikiInput) # single article, [0] is title, [1] is links
            dic[element[0]] = element[1]
            count += 1
            if count % 1000000 == 0:
                print('loaded ' + format(count, ',d') + ' elements')
        except EOFError:
            break # breaks when all articles have been read
    endTime = time.clock()
    print('Time to load dictionary: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    wikiInput.close()
    return dic

def aStar(dic, start, end, stopTime):
    '''
    Runs the A Star Algorithm on the passed dictionary
    dic (dictionary): the dictionary containing the articles' data
    start (String): the title of the start article
    end (String): the title of the end article
    stopTime (int): the number of seconds to find a path before it breaks
    Returns:
        True if path found
        False if no path was found
    '''
    openList = set()   # the articles that can be got to, but have not be look at
    closedList = set() # the articles that have already be processed
    distances = {}     # holds the distances for each article from the start
    parents = {}       # holds the parent article for the best path for the articles

    distances[start] = 0
    openList.add(start)
    startTime = time.clock()
    
    while openList:
        if time.clock() - startTime >= stopTime:
            return False # returns False if it takes longer the time passed
        
        start = sorted(openList, key=lambda inst: distances[inst])[0]
        openList.remove(start)
        closedList.add(start)
        for article in dic[start].split(':'):
            if article in dic: # if the article is an actual link, not a red wiki link
                if article not in closedList:
                    distances[article] = distances[start] + 1
                    openList.add(article)
                    parents[article] = start
                if distances[article] > distances[start] + 1: # overwrites path if a better one is found
                    distances[article] = distances[start] + 1
                    parents[article] = start
                if article == end:
                    return parents
    return False
          
def pathMaker(parents, start, end):
    '''
    Makes the list of articles to go to to get from the start to the finish
    dic (dictionary): the dictionary of the articles
    start (String): the start article's name
    end (String): the end article's name
    Returns:
        the list of the articles to go to
    '''
    path = []
    while not end == start:
        path.append(end)
        end = parents[end]
    path.append(start)
    path.reverse()
    return path

def main():
    '''
    Test data / code
    '''
    start = 'Anarchism'
    end = 'Jurisdiction'
    dic = makeDic('output.txt')
    startTime = time.clock()
    parents = aStar(dic, start, end, 60)
    endTime = time.clock()
    print('Time to find path: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    print('-----------------------------------------')
    print(pathMaker(parents, start, end))

#main()
