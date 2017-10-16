from wsgiref.simple_server import make_server

import httputils, urls

def wydra(environ, start_response):
    """ WSGI callable. """
    http_method = environ['REQUEST_METHOD']
    request_body = environ['wsgi.input']
    resource_name, resource_id = httputils.extract_path(environ['PATH_INFO'])
    urls.mapping[http_method][resource_name](resource_id, request_body)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ret

if __name__ == '__main__':
    make_server(host='localhost', port=8080, app=wydra).serve_forever()
