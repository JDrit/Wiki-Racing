import datetime
import time
import cPickle as pickle


def readFile(fname):
    output = open('output2.txt', 'w')
    f = open(fname)  # the xml file to read from
    start = False
    pageTitle = ''  # article's title
    links = ''  # article's links
    entry = []
    count = 0

    line = f.readline()
    while not line == '':
        if '<text' in line or start:
            start = True
            while '[[' in line:
                link = line[line.find('[[') + 2:line.find(']]')]
                if '|' in link:  # removes the second part of the link
                    link = link[:link.find('|')]
                if '#' in link:  # this removes the href second part of a link
                    link = link[:link.find('#')]
                if not ':' in link:  # if it has a ':', it is a file or something
                    if not link == '':
                        link = link[0].upper() + link[1:]  # uppercases the first letter
                    links += link + ':'
                line = line[line.find(']]') + 2:]
        if '<title>' in line:
            pageTitle = line[11:-9]
        if '</text>' in line:
            if not len(links) == 1:  # one link means it is a redirect
                count += 1
                # removes the last ':' for breaking the String into a list
                links = links[:-1]
                entry = [pageTitle, links]
                pickle.dump(entry, output)
            start = False
            links = ''
            entry = []
            if count % 1000000 == 0:
                print(format(count, ",d") + " done.")
        line = f.readline()
    f.close()
    output.close()
    print('element count: ' + format(count, ",d"))


start = time.clock()
readFile('C:\Users\JD\My Documents\wikipedia files\enwiki-latest-pages-articles'
         '.xml\enwiki-latest-pages-articles.xml')
end = time.clock()
print('time diff: ' + str(datetime.timedelta(seconds=(end - start))))
