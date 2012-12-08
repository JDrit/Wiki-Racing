'''
author: JDrit
description: This runs in the background, finding paths that could not be found
        the webserver. When a path is not found, it is added to the fail database
        and than read into a worker thread that gives it a longer time to find the
        path. Once a path is found it is added to the database. If there are no
        failed paths, then the program picks a common start and end article and
        finds the path between them.
'''
from pathfinder import pathMakerString, BFS
import sqlite3
import Queue
import threading

queue = Queue.Queue() # the queue of the paths to find
dic = {}              # the dictionary of the aritcles and their links
currentArticles = []  # the list of paths currently being worked on

class WorkerThread(threading.Thread):
        '''
        The class that does the extended path finding between the two given
                articles. There can be many of this class running at the same
                time.
        '''
        def __init__(self, queue):
                threading.Thread.__init__(self)
                self.queue = queue
                print('worker thread started')

        def run(self):
                '''
                Tries to find the path between two articles, given in the queue.
                        It blocks till their is a job in the queue to do.
                '''
                global dic
                global currentArticles
                conn = sqlite3.connect('db.db')
                cur = conn.cursor()

                while True:
                        job = self.queue.get(True) # blocks till their is a job in the queue
                        if not job == None:
                                print('started job', job, 'jobs left', queue.qsize())
                                start = str(job).split(':')[0]
                                end = str(job).split(':')[1]
                                currentArticles.append(start + ':' + end) # tells the server what is currently being worked on
                                parents = BFS(dic, start, end, 600)[0] # the holding point
                                if parents:
                                        pathString = pathMakerString(parents, start, end)
                                        print('completed job', job)
                                        cur.execute("INSERT INTO paths VALUES ('%s', '%s', '%s')" % (start, end, pathString))
                                else:
                                        print('failed job', job)
                                cur.execute("DELETE FROM fails WHERE start='%s' AND end='%s'" % (start, end))
                                conn.commit()
                                currentArticles.remove(start + ':' + end)
                        self.queue.task_done()

class MainThread(threading.Thread):
        '''
        The class that runs the WorkerThread classes and adds new elements to the
                queue. There is only one of this type of thread running at a time.
        '''
        def __init__(self, queue, threadCount):
                threading.Thread.__init__(self)
                self.queue = queue
                self.threadCount = threadCount

        def run(self):
                '''
                Starts the worker threads and adds new searches to the queue when
                        the queue is empty.
                '''

                getAllFails()
                
                for i in range(self.threadCount):
                        t = WorkerThread(queue)
                        t.setDaemon(True)
                        t.start()                

                while True:
                        if queue.empty() and not dic == {}:
                                newSearch = addNewSearch()
                                if not newSearch == None:
                                        print('added new seach', newSearch)
                                        queue.put(newSearch)
                queue.join()
  

def getAllFails():
        '''
        Reads in the failed attempts from the database and addes them to the
                queue.
        '''
        global queue
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        failsCur = cur.execute("SELECT * FROM fails").fetchall()
        for element in failsCur:
                queue.put(str(element[0]) + ':' + str(element[1]))
                currentArticles.append(str(element[0]) + ':' + str(element[1]))
        print('Read in ' + str(len(failsCur)) + ' failed attempts from the database')
        

def addElement(start, end):
        '''
        Adds an element to the queue to find the path of. This is called by the
                server itself when it can not find a path in the short timeframe.
        start (String): the title of the start article
        end (String): the title of the end article
        '''
        global queue
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        if cur.execute("SELECT * FROM fails WHERE start='%s' AND end='%s'" % (start, end)).fetchall() == []:
                cur.execute("INSERT INTO fails VALUES ('%s', '%s')" % (start, end))
                conn.commit()
                queue.put(start + ':' + end)
                print('addElement', start + ':' + end + ' :: Search List Length: ' + str(queue.qsize()))
                

def addNewSearch():
        '''
        Adds a new start and end element to the queue to find the path of. This
                is called when there are no more failed attempts in the queue.
        '''
        global dic
        global currentArticles
        
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        startLocs = []
        endLocs = []
        start = ''
        end = ''
        
        startCur = cur.execute('''SELECT start, COUNT(*) 'start_count'
                                FROM paths
                                GROUP BY start
                                ORDER BY start_count DESC, start
                                ''').fetchall()
        endCur = cur.execute('''SELECT end, COUNT(*) 'end_count'
                                FROM paths
                                GROUP BY end
                                ORDER BY end_count DESC, end
                                ''').fetchall()
        for element in startCur:
                startLocs.append(str(element[0]))
        for element in endCur:
                endLocs.append(str(element[0]))
        while True:
                if len(startLocs) > 0:
                        start = startLocs.pop(0)
                else:
                        return
                if len(endLocs) > 0:
                        end = endLocs.pop(0)
                else:
                        return

                if cur.execute("SELECT path FROM paths WHERE start='%s' AND end='%s'" % (start, end)).fetchall() == []:
                        if not start + ':' + end in currentArticles:
                                break
        currentArticles.append(start + ':' + end)
        return start + ':' + end



def startBackend(dictionary, threadCount):
        '''
        Starts all main thread that controls all the worker threads.
        dictionary (dict): the dictionary of all the articles' titles and links
        threadCount (int): the number of worker threads to be run
        '''
        global dic
        dic = dictionary

        t = MainThread(queue, threadCount)
        t.setDaemon(True)
        t.start()
        print('main backend thread started')

