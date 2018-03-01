#Nelson Hsiao 2/28/18
#nhsiao-hw4

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json

f = open('cve.json', 'r')
db = json.loads(f.read())
f.close()

#print len(db)

def help_view(request):
	return Response('type in address bar /find/ followed by what word your looking for.')

def find_view(request):
	output = ''
	mydict = request.matchdict
	for item in db:
		value = mydict['query']
		obj = item.lower()

		if value.lower() in obj.split():
			output += item + '<br/>'

	if output != '':
		return Response(output)
	else:
		return Response('nothing found')

#def hello_world(request):
	#print request.matchdict
	#j = request.matchdict
	#return Response('Hello %(name)s!' % request.matchdict)
print "Server Running"

if __name__ == '__main__':

	#cearting a instance of the config class
    with Configurator() as config:
    	#add router
    	config.add_route('home', '/home')
    	config.add_view(help_view, route_name='home')

        config.add_route('find', '/find/{query}')
        config.add_view(find_view, route_name='find')

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()