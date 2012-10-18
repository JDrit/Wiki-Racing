import datetime
import time
import cPickle as pickle

def readFile(fname):
    output = open('output.txt', 'w')
    f = open(fname) # the xml file to read from
    start = False
    pageTitle = ''  # article's title
    links = []      # article's links
    entry = []
    count = 0
    
    line = f.readline()
    while not line == '': 
        if '<text' in line or start:
            start = True
            while '[[' in line:
                link = line[line.find('[[') + 2 : line.find(']]')]
                if ':' in link: # dont use link, it is a file or something
                    pass
                elif '|' in link: # removes the second part of the link
                    link = link[:link.find('|')]
                    links.append(link)
                else:
                    links.append(link)
                line = line[line.find(']]') + 2:]       
        if '<title>' in line:
            pageTitle = line[11 : -9]
        if '</text>' in line:
            if not len(links) == 1: # one link means it is a redirect
                count += 1
                entry = [pageTitle, links]
                pickle.dump(entry, output)
            start = False
            links = []
            entry = []
            if count % 1000 == 0:
                print(str(count) + " done.")
        line = f.readline()   
    f.close()
    output.close()
    print('element count: ', count)
    
start = time.clock()
readFile('C:\Users\JD\My Documents\wikipedia files\enwiki-latest-pages-articles.xml\enwiki-latest-pages-articles.xml')
end = time.clock()
print('time diff: ' + str(datetime.timedelta(seconds=(end - start))))



