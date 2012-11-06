from bottle import Bottle, redirect, route, run, post, request, get, template, error, static_file
from pathfinder import pathMaker, makeDic, aStar
import logging
from time import localtime, strftime

dic = {}

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
    startLoc = request.forms.get('start')
    endLoc = request.forms.get('end')
    #logging.info(' POST ' + request.environ.get('REMOTE_ADDR') + ' ' + request.path + ' [' + strftime("%a, %d %b %Y %H:%M:%S", localtime()) + '] ' + startLoc + ' : ' + endLoc)
    
    if startLoc in dic and endLoc in dic:
        parents, time = aStar(dic, startLoc, endLoc, 90)
        if parents:
            path = pathMaker(parents, startLoc, endLoc)
            output = template('pathViewer', path=path, time=str('%.2f' % time))
        else:
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
    dic = makeDic('../output.txt')
    run( host='localhost', port=8080)

serverStart()  


