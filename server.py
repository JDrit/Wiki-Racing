from bottle import redirect, run, post, request, get, template, error
from pathfinder import pathMaker, makeDic, aStar

dic = {}

@get('/path')
def index():
    output = template('index', message = 'Enter in a start and end point.')
    return output

@post('/path')
def pathfinder():
    global dic
    startLoc = request.forms.get('start')
    endLoc = request.forms.get('end')
    if startLoc in dic and endLoc in dic:
        parents = aStar(dic, startLoc, endLoc, 60)
        if parents:
            path = pathMaker(parents, startLoc, endLoc)
            output = template('pathViewer', path=path)
        else:
            output = template('index', message = 'There is no path between the two given points.')
    else:
        output = template('index', message = 'Either the start location or end location is not a valid article page')
    return output
            
@error(404)
def error404(error):
    redirect('/path')

@error(500)
def error505(error):
    output = template('index', message = 'The server is having some trouble processing your request right now')
    return output

def serverStart():
    global dic
    print('Server Started')
    dic = makeDic('output.txt')
    print('Dictionary Loaded')
    run(host='localhost', port=8080)

serverStart()  


