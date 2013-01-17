'''
author: JDrit
description: The library that does all the processing for the server. This loads
    the data, finds the path, and finds the string of the path.
'''
from time import clock
import datetime
import cPickle as pickle
from collections import deque


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
    startTime = clock()
    while True:
        try:
            element = pickle.load(wikiInput)  # single article, [0] is title, [1] is links
            dic[element[0]] = element[1]
            count += 1
            if count % 1000000 == 0:
                print('loaded ' + format(count, ',d') + ' elements')
        except EOFError:
            break  # breaks when all articles have been read
    endTime = clock()
    print('Time to load dictionary: ' + str(datetime.timedelta(
                                            seconds=(endTime - startTime))))
    print('Loaded ' + str(len(dic)) + ' elements')
    wikiInput.close()
    return dic


def BFS(dic, start, end, stopTime):
    '''
    Preforms a Breth First Search on the Wikipedia articles to find the shortest
        path between the start and end
    dic (dict): the dictionary of the Wikipedia articles' titles and links
    start (str): the start article's title
    end (str): the end article's title
    stopTime (int): the number of seconds to timeout if a path can not be found
    Returns:
        parents (dict): the parent of all articles in the searched area
        time (int): the number of seconds it took to find the path
    '''
    parents = {}
    queue = deque()
    queue.append(start)
    startTime = clock()

    while not len(queue) == 0:
        if clock() - startTime >= stopTime and not stopTime - 1:
            return False, 0
        current = queue.popleft()
        if current == end:
            return parents, (clock() - startTime)
        for neighbor in dic[current].split(':'):
            if neighbor not in parents and neighbor in dic:
                parents[neighbor] = current
                queue.append(neighbor)
    return False, 0


def pathMaker(parents, start, end):
    '''
    Makes the list of articles to go to to get from the start to the finish
    parents (dictionary): the dictionary of the articles and their parents
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


def pathMakerString(parents, start, end):
    '''
    Makes a string that represents the articles to go through to get from the
        start to the end article
    parents (dictionary): the dictionary of the articles and their parents
    start (String): the start article's name
    end (String): the end article's name
    Returns:
        a string of the path to take
    '''
    path = pathMaker(parents, start, end)
    s = ''
    for element in path:
        s += element + ":"
    return s[:-1]


def main():
    '''
    Test data / code
    '''
    start = 'USA'
    end = 'Akron'
    dic = makeDic('output.txt')
    startTime = clock()
    print(len(dic))
    parents, _ = BFS(dic, start, end, -1)
    endTime = clock()
    print('Time to find path: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
    print('-----------------------------------------')
    print(pathMaker(parents, start, end))

#main()
