import sqlite3
import time
import datetime
import cPickle as pickle
#from priodict import priorityDictionary


class Node:
   
    def __init__(self, title, links):
        self.title = title   # the title of the article
        self.links = links   # the titles of all the articles linked to
        self.parent = None   # the parent article title for path finding
        self.distance = -1   # the number of articles it takes to get to


def makeDic():
   f = open('output.txt')
   dic = {}
   count = 0
   while True:
      try:
         element = pickle.load(f)
         dic[element[0]] = Node(element[0], element[1].split(':'))
         count += 1
         if count % 1000000 == 0: print('loaded ' + str(len(dic)) + ' elements')
         #dic.update(pickle.load(f))
      except EOFError:
         break
   print(len(dic))
   return dic

def main(start, end):
    #conn = sqlite3.connect('wiki.db')
    #conn.text_factory = str
    dic = makeDic()
    print('imported dictionary')
    print(len(dic))
    distances = {}
    previous = {}
    Q = priorityDictionary()
    Q[start] = 0

    for page in Q:
        distances[page] = Q[page]
        if page == end:
            break
        for link in dic[page]:
            #print('article: ' + article)
            length = distances[page] + 1
            if link in distances:
                if length < distances[link]:
                   raise ValueError
            elif link not in Q or length < Q[link]:
                Q[link] = length
                previous[link] = page
        print(page)
    return (distances, previous)

def aStar(dic, start, end):
   openList = set()
   closedList = set()
   

   openList.add(start)
   while openList:
      start = sorted(openList, key=lambda inst:dic[inst].distance)[0]
      print('start: ' + str(start))
      if start == end:
         print('done')
         return pathmaker(start)
      openList.remove(start)
      closedList.add(start)
      print(dic[start].links)
      for article in dic[start].links:
          print('article: ' + str(article))
          if article not in closedList:
              dic[article].distance = dic[start].distance + 1
              if article not in openList:
                  openList.add(article)
                  dic[article].parent = start

def pathmaker(start):
   path = {}
   count = 1
   while not node.parent == None:
      path[count] = node
      node = node.parent
      count += 1
   return path

            
'''conn = sqlite3.connect('wiki.db')
conn.text_factory = str       
lst = str(conn.execute('SELECT links FROM pages WHERE name = "%s"' % 'New York Philharmonic').fetchone())[2:-4].split(':')
print(lst)'''
start = 'Kathrinstadt Airport'
end = 'Federal Aviation Administration'
startTime = time.clock()
print(aStar(makeDic(), start, end))
'''distances, previous = main(start, end)
path = []
while True:
   path.append(end)
   if end == start:
      break
   end = previous[end]
endTime = time.clock()
print('Path:')
for i in path:
   print('- ' + i)
print('Time: ' + str(datetime.timedelta(seconds=(endTime - startTime))))
print('done')'''
