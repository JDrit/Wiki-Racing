from bottle import route, redirect, run, post, request, get, template, error
from pathfinder import pathMaker, makeDic, aStar

dic = {}

@get('/path')
def index():
    return '''
            <form method="POST" action="/path">
                <input name="start" type="text" />
                <input name="end" type="text" />
                <input type="submit" />
            </form>
            '''

@post('/path')
def pathfinder():
    global dic
    startLoc = request.forms.get('start')
    endLoc = request.forms.get('end')
    if startLoc in dic and endLoc in dic:
        print('locations are good')
        if aStar(dic, startLoc, endLoc):
            print('found path')
            path = pathMaker(dic, startLoc, endLoc)
            print(path)
            output = template('pathViewer', path=path)
            return output
        else:
            return '<p>No Connection between <b>' + startLoc + '</b> and <b>' + endLoc + '</b>.</p>'
    else:
        return 'Either the start location or end location is not a valid article page'
        
@error(404)
def error404(error):
    redirect('/path')

@error(500)
def error505(error):
    return 'The server is having some trouble processing your request right now'

def serverStart():
    global dic
    print('Server start')
    dic = makeDic('output.txt')
    run(host='localhost', port=8080)

serverStart()  


