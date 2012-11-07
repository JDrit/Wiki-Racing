from bottle import Bottle, redirect, route, run, post, request, get, template, error, static_file
from pathfinder import pathMaker, makeDic, aStar, pathMakerString
from time import localtime, strftime
import logging, sqlite3

dic = {}
conn = sqlite3.connect('paths.db')
cur = conn.cursor()

@route('/static/:path#.+#', name='static')
def static(path): # deals with the static .css and .js files
    return static_file(path, root='static')

@get('/')
def index():
    #logging.info(' GET ' + request.environ.get('REMOTE_ADDR') + ' ' + request.path + ' [' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + ']')
    output = template('index', message = 'Enter in a start and end point.')
    return output

@post('/')
def pathfinder():
    global dic
    global cur
    
    startLoc = request.forms.get('start')
    endLoc = request.forms.get('end')
    #logging.info(' POST ' + request.environ.get('REMOTE_ADDR') + ' ' + request.path + ' [' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + '] ' + startLoc + ' : ' + endLoc)
    
    if startLoc in dic and endLoc in dic: # if both locations exist
        sqlElement = str(cur.execute("SELECT path FROM paths WHERE start='%s' AND end='%s'" % (startLoc, endLoc)).fetchone())[3:-3]
        if sqlElement: # if the start and end loc have already been found
            output = template('pathViewer', path=sqlElement.split(":"), time='0.00')
        else: # if new start and end location
            parents, time = aStar(dic, startLoc, endLoc, 90)

            if parents: # if a path was found
                pathString = pathMakerString(parents, startLoc, endLoc)
                cur.execute("Insert INTO paths VALUES ('%s', '%s', '%s')" % (startLoc, endLoc, pathString))
                output = template('pathViewer', path=pathString.split(':'), time=str('%.2f' % time))
            else: # no path found
                output = template('index', message = 'There is no path between the two given points.')
    else:
        output = template('index', message = 'Either the start location or end location is not a valid article page')
    return output
            
@error(404)
def error404(error):
    #logging.error(' 404 ' + request.environ.get('REMOTE_ADDR') + ' ' + request.path + ' [' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + ']')
    output = template('index', message = 'Enter in a start and end point.')
    return output 

@error(500)
def error505(error):
    #logging.error(' 500 ' + request.environ.get('REMOTE_ADDR') + ' ' + request.path + ' [' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + ']')
    output = template('index', message = 'The server is having some trouble processing your request right now')
    return output

def serverStart():
    global dic
    #logging.basicConfig(filename='logs/' + strftime('%Y-%m-%d-%H-%M', localtime()) + '.log', level=logging.INFO)
    #logging.info(' Server started at ' + strftime("%a, %d %b %Y %H:%M:%S ", localtime()))
    print('Server started')
    dic = makeDic('output.txt')
    run( host='localhost', port=8080)

serverStart()  


